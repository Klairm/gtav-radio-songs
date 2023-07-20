
  ## Script to save URI tracks from gtaV
  
  This simple scripts adds the URI tracks from gtaV, that you can get using: https://github.com/Klairm/violentmonkey-scripts
  the browser scripts searchs for your socialclub profile to get all the songs you shared in-game from the GTA V radio.

  #### Usage

  Grab your `uri_tracks.txt` file you got from the violentmonkey script and place it in the same folder where this python script is located.

  <b> IMPORTANT:</b>  you need to place your `client_id` and `client_secret` in the script, also you need to replace the playlist ID where you'll save the songs.

  If you don't know how to get the `client_id` and `client_secret`, you can do the following:


```
    1. Browse to https://developer.spotify.com/dashboard/applications.

    2. Log in with your Spotify account.

    3. Click on ‘Create an app’.

    4. Pick an ‘App name’ and ‘App description’ of your choice and mark the checkboxes.

    After creation, you see your ‘Client Id’ and you can click on ‘Show client secret` to unhide your ’Client secret’.
```

  Then simple double click the .py file or run the command `python main.py`
  

  ## TODO:
   - Make this a web app, so the user just has to put the playlist ID.

  