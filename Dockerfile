FROM odoo:18

USER root

RUN pip3 install --no-cache-dir --break-system-packages \
    fsspec s3fs \
    packaging

USER odoo
