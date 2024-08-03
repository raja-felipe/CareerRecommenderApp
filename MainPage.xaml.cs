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
        

        private void OnCounterClicked(object sender, EventArgs e)
        {
            if (mediaElement.CurrentState == MediaElementState.Paused) { mediaElement.Play(); }
            else if (mediaElement.CurrentState == MediaElementState.Playing) { mediaElement.Pause(); }

            ProcessStartInfo python_script_test = new ProcessStartInfo();
            python_script_test.FileName = "test_python.py";


            
        }
    }

}
