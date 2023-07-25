from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.set_xml_ids_noupdate_value(
        env,
        "website_payment",
        [
            "mail_template_donation",
        ],
        True,
    )
