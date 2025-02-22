using System;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
// Assume these namespaces correspond to Jellyfin's internal classes.
// using Jellyfin.Server.Providers;
// using Jellyfin.Server.Implementations;
using Jellyfin.Data.Entities; // For BaseItem and MediaStreamType

namespace Jellyfin.Plugins.SubtitleGrabber
{
    public class SubtitleCheckerService : IHostedService, IDisposable
    {
        private readonly ILibraryManager _libraryManager;
        private readonly ILogger<SubtitleCheckerService> _logger;
        private Timer _timer;

        public SubtitleCheckerService(ILibraryManager libraryManager, ILogger<SubtitleCheckerService> logger)
        {
            _libraryManager = libraryManager;
            _logger = logger;
        }

        public Task StartAsync(CancellationToken cancellationToken)
        {
            _logger.LogInformation("SubtitleChecker Service starting.");
            _timer = new Timer(CheckLibrary, null, TimeSpan.Zero, TimeSpan.FromHours(25));
            return Task.CompletedTask;
        }

        private async void CheckLibrary(object state)
        {
            try
            {
                _logger.LogInformation("Scanning media library for subtitle-less items.");

                var movies = _libraryManager.GetItemsByType("Movie");
                foreach (var movie in movies)
                {
                    if (!HasSubtitles(movie))
                    {
                        _logger.LogInformation($"Movie '{movie.Name}' does not have subtitles.");
                        // TODO: Trigger subtitle download via OpenSubtitles API.
                    }
                }

                var episodes = _libraryManager.GetItemsByType("Episode");
                foreach (var episode in episodes)
                {
                    if (!HasSubtitles(episode))
                    {
                        _logger.LogInformation($"Episode '{episode.Name}' does not have subtitles.");
                        // TODO: Trigger subtitle download.
                    }
                }
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error during library scan.");
            }
        }

        private bool HasSubtitles(BaseItem item)
        {
            return item.MediaStreams?.Any(stream => stream.Type == MediaStreamType.Subtitle) ?? false;
        }

        public Task StopAsync(CancellationToken cancellationToken)
        {
            _logger.LogInformation("SubtitleChecker Service stopping.");
            _timer?.Change(Timeout.Infinite, 0);
            return Task.CompletedTask;
        }

        public void Dispose()
        {
            _timer?.Dispose();
        }
    }
}
