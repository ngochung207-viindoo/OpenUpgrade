from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(
        env.cr, "website_slides_survey", "16.0.1.0/noupdate_changes.xml"
    )
