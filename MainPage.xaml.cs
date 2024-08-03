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

        public void CallPython()
        {
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
            startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
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
