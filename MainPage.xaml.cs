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
        
        private void CallPython(object sender, EventArgs q)
        {
            Runtime.PythonDLL = @"C:\Users\finnc\AppData\Local\Programs\Python\Python311\python311.dll";
            {


                PythonEngine.Initialize();
                using (Py.GIL())
                {

                    dynamic sys = Py.Import("sys");
                    sys.path.append(Path.Combine("C:\\Users\\finnc\\source\\repos\\CareerRecommenderApp\\"));
                    var test = Py.Import("Test");
                    var result = test.InvokeMethod("helloWorld");

                }
            }
        }
        private void OnCounterClicked(object sender, EventArgs e)
        {
            if (mediaElement.CurrentState == MediaElementState.Paused) { mediaElement.Play(); }
            else if (mediaElement.CurrentState == MediaElementState.Playing) { mediaElement.Pause(); }

            


            
        }
    }

}
