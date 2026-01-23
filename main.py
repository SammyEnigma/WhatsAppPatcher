import argparse
from stitch import Stitch
from artifactory_generator.fmessage import FMessage
from artifactory_generator.dex_copier import DexCopier
from artifactory_generator.signature_finder import SignatureFinder
from artifactory_generator.decrypt_protobuf_finder import DecryptProtobufFinder


def get_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-p', '--apk-path', dest='apk_path', help='APK path', required=True)
    parser.add_argument('-o', '--output', dest='output', help='Output APK path', required=False, default='output.apk')
    parser.add_argument('-t', '--temp', dest='temp_path', help='Temp path for extracted content', required=False,
                        default='./temp')
    parser.add_argument('-g', '--google-api-key', dest='api_key', help='Custom google api key', required=False, default=None)
    parser.add_argument('--artifactory', dest='artifactory', help='Artifactory path', required=False,
                        default='./artifactory.json')
    return parser.parse_args()


def main():
    args = get_args()
    artifactory_list = [
        FMessage(args),
        DexCopier(args),
        SignatureFinder(args),
        DecryptProtobufFinder(args),
    ]
    with Stitch(
        apk_path=args.apk_path,
        output_apk=args.output,
        temp_path=args.temp_path,
        artifactory_list=artifactory_list,
        google_api_key=args.api_key,
        external_module='./smali_generator'
    ) as stitch:
        stitch.patch()


if __name__ == '__main__':
    main()
