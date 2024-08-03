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
            Runtime.PythonDLL = @"C:\Users\finnc\AppData\Local\Programs\Python\Python312\python312.dll";
            PythonEngine.Initialize();
            
            using (Py.GIL())
            {
                var recommendSys = Py.Import("Test");
                var result = recommendSys.InvokeMethod(recommendSys);

            }
        }
        private void OnCounterClicked(object sender, EventArgs e)
        {
            if (mediaElement.CurrentState == MediaElementState.Paused) { mediaElement.Play(); }
            else if (mediaElement.CurrentState == MediaElementState.Playing) { mediaElement.Pause(); }

            


            
        }
    }

}
