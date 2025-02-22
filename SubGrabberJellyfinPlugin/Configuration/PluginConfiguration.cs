
using MediaBrowser.Model.Plugins;
class PluginConfiguration : BasePluginConfiguration
{
    public string JellyfinServerAddress { get; set; }
    public string JellyfinApiKey { get; set; }
    public string JellyfinLibraryId { get; set; }
    public string JellyfinUserId { get; set; }
    public string JellyfinUserName { get; set; }
    public string JellyfinUserPassword { get; set; }
    public string JellyfinUserToken { get; set; }
    public string JellyfinUserTokenExpiry { get; set; }
    public string JellyfinUserTokenExpiryDate { get; set; }
    public string JellyfinUserTokenExpiryTime { get; set; }
    public string JellyfinUserTokenExpiryDateTime { get; set; }
    public string JellyfinUserTokenExpiryDateTimeUtc { get; set; }
    public string JellyfinUserTokenExpiryDateTimeLocal { get; set; }
    public string JellyfinUserTokenExpiryDateTimeLocalUtc { get; set; }
    public string JellyfinUserTokenExpiryDateTimeLocalUtcString { get; set; }
    public string JellyfinUserTokenExpiryDateTimeLocalUtcStringFormatted { get; set; }
    public string JellyfinUserTokenExpiryDateTimeLocalUtcStringFormattedShort { get; set; }
    public string JellyfinUserTokenExpiryDateTimeLocalUtcStringFormattedLong { get; set; }
    public string JellyfinUserTokenExpiryDateTimeLocalUtcStringFormattedFull { get; set; }
    public string JellyfinUserTokenExpiryDateTimeLocalUtcStringFormattedFullShort { get; set; }
    public string JellyfinUserTokenExpiryDateTimeLocalUtcStringFormattedFullLong { get; set; }
    public string JellyfinUserTokenExpiryDateTimeLocalUtcStringFormattedFullFull { get; set; }
    public string JellyfinUserTokenExpiryDateTimeLocalUtcStringFormattedFullFullShort { get; set; }
    public string JellyfinUserTokenExpiryDateTimeLocalUtcStringFormattedFullFullLong { get; set; }
    public string JellyfinUserTokenExpiryDateTimeLocalUtcStringFormattedFullFullFull { get; set; }
    public string JellyfinUserTokenExpiryDateTimeLocalUtcStringFormattedFullFullFullShort { get; set; }
    public string JellyfinUserTokenExpiryDateTimeLocalUtcStringFormattedFullFullFullLong { get; set; }
    public string JellyfinUser
    {
        get
        {
            return JellyfinUserName;
        }
    }
    public string JellyfinUserTokenExpiryDateTimeLocalUtcStringFormattedFullFullFullFull { get; set; }
    public string JellyfinUserTokenExpiryDateTimeLocalUtcStringFormattedFullFullFullFullShort { get; set; }
}