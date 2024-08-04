using CommunityToolkit.Maui.Views;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using System.ComponentModel;

namespace CareerRecommenderApp.ViewModel;

public partial class MainViewModel : ObservableObject
{

    [ObservableProperty]
    string file;

    [RelayCommand]
    void Swipe(SwipedEventArgs e)
    {
        switch(e.Direction)
        {
            case SwipeDirection.Up:
                file = "VideoStorage/Degree.mp4";
                break;
            case SwipeDirection.Down:
                file = "VideoStorage/DeloitteShort.mp4";
                break;


        }

        
    }

    
    public Uri Media()
    {
        return new Uri(file);
    }

    
        

}

