from flask import  request, Response

contenttypes = {
    "MSC": "text/plain",
    "MSCE": "text/plain",
    "HTML": "text/html",
    "PDF": "application/pdf"
}

suffix = {
    "MSC": "msc",
    "MSCE": "msce",
    "HTML": "html",
    "PDF": "pdf"
}


class DownloadFileHander:
    @staticmethod
    def post():
        type = request.form.get('type')
        content = request.form.get('content')

        if type not in ["MSC", "MSCE", "HTML", "PDF"]:
            # TODO
            return "TODO"
            # fullfname = "./excelinterop/phpexcel/socialcalc/tmp/tmp"
            # inpfile = fullfname + ".b"

            # with codecs.open(inpfile, encoding='utf-8', mode="w+") as f:
            #     f.write(content)

            # outfile = fullfname + "." + suffix.get(type, "txt")
            # logging.info(outfile)
            # logging.info(inpfile)
            # cmdname = "./excelinterop/phpexcel/socialcalc/export.php"
            # output = subprocess.getoutput(f"php {cmdname} {inpfile} {outfile} {type}")
            # logging.info(output)

            # with open(outfile, 'rb') as f:
            #     content = f.read()

        elif type == "PDF":
            # TODO
            return "TODO"
            # logging.info("type is PDF")
            # fullfname = "/home/ubuntu/tmp/tmp"
            # inpfile = fullfname + ".html"

            # with codecs.open(inpfile, encoding='utf-8', mode="w+") as f:
            #     f.write(content)

            # outfile = fullfname + "." + suffix.get(type, "pdf")
            # logging.info(outfile)
            # logging.info(inpfile)
            # cmdname = "/usr/local/bin/wkhtmltopdf.sh"
            # output = subprocess.getoutput(f"{cmdname} {inpfile} {outfile}")
            # logging.info(output)

            # with open(outfile, 'rb') as f:
            #     content = f.read()

        else:
            # This assumes the content is directly returned if it's a supported type without conversion
            content = content.encode('utf-8')

        response = Response(content)
        response.headers['Content-Type'] = contenttypes.get(type, 'application/octet-stream')
        response.headers['Content-Disposition'] = f'attachment; filename="tmp.{suffix.get(type, "txt")}"'
        response.headers['Cache-Control'] = 'max-age=0'

        return response