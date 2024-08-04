using CommunityToolkit.Maui.Core.Primitives;
using System.Diagnostics;
using Python.Runtime;
using CareerRecommenderApp.ViewModel;


namespace CareerRecommenderApp
{
    public partial class MainPage : ContentPage
    {
        
        
        public MainPage(MainViewModel vm)
        {
            InitializeComponent();
            BindingContext = vm;
        }
        
        
        private void OnCounterClicked(object sender, EventArgs e)
        {
            if (mediaElement.CurrentState == MediaElementState.Paused) { mediaElement.Play(); }
            else if (mediaElement.CurrentState == MediaElementState.Playing) { mediaElement.Pause(); }

                        
        }
        

        
    }

}
