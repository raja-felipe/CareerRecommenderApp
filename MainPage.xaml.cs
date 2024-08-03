using CommunityToolkit.Maui.Core.Primitives;
using System.Diagnostics;
using Python.Runtime;

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
            Runtime.PythonDLL = @"C:\Users\finnc\anaconda3\python311.dll";
            PythonEngine.Initialize();
            
            using (Py.GIL())
            {
                var recommendSys = Py.Import("");
                var result = recommendSys.Invoke();

            }
        }
        private void OnCounterClicked(object sender, EventArgs e)
        {
            if (mediaElement.CurrentState == MediaElementState.Paused) { mediaElement.Play(); }
            else if (mediaElement.CurrentState == MediaElementState.Playing) { mediaElement.Pause(); }

            


            
        }
    }

}
