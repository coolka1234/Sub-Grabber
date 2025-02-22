using MediaBrowser.Common.Plugins;
class Plugin : BasePlugin<PluginConfiguration>
{
    public Plugin(IApplicationPaths applicationPaths, IXmlSerializer xmlSerializer)
        : base(applicationPaths, xmlSerializer)
    {}
    public override string Name
    {
        get
        {
            return "SubGrabberJellyfinPlugin";
        }
    }
    public override Guid Id => new Guid("ef0f6444-3ac0-4e73-bef7-2ca25225dffb");
}