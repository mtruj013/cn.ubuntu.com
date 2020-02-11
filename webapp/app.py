from canonicalwebteam.blog import BlogViews
from canonicalwebteam.blog.flask import build_blueprint
from canonicalwebteam.flask_base.app import FlaskBase
from canonicalwebteam.templatefinder import TemplateFinder

app = FlaskBase(
    __name__,
    "cn.ubuntu.com",
    template_folder="../templates",
    static_folder="../static",
    template_404="templates/404.html",
    template_500="templates/500.html",
)

template_finder_view = TemplateFinder.as_view("template_finder")
app.add_url_rule("/", view_func=template_finder_view)
app.add_url_rule("/<path:subpath>", view_func=template_finder_view)

blog_views = BlogViews(tag_ids=[3265], blog_title="博客", per_page=11)
blog_blueprint = build_blueprint(blog_views)
app.register_blueprint(blog_blueprint, url_prefix="/blog")
