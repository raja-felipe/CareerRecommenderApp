using CommunityToolkit.Maui.Core.Primitives;
using System.Diagnostics;

namespace CareerRecommenderApp
{
    public partial class MainPage : ContentPage
    {
        int count = 0;

        public MainPage()
        {
            InitializeComponent();
        }

        private void CallPython(object sender, EventArgs a)
        {
            Process process = new Process();
            ProcessStartInfo startInfo = new ProcessStartInfo();
            startInfo.WindowStyle = ProcessWindowStyle.Normal;
            startInfo.FileName = "Python.exe";
            startInfo.Arguments = "testIntegration.py";
            process.StartInfo = startInfo;
            process.Start();
        }
        private void OnCounterClicked(object sender, EventArgs e)
        {
            if (mediaElement.CurrentState == MediaElementState.Paused) { mediaElement.Play(); }
            else if (mediaElement.CurrentState == MediaElementState.Playing) { mediaElement.Pause(); }

            


            
        }
    }

}
