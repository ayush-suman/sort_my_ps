# What it does
Sort My PS quickly sorts your PS preference list based on the following parameters - 
1. Industry preference (IT, Electronics, Chemical etc.)
2. Stipend (If you choose to use sorting based on stipend)
3. Location preference (Bangalore, Mumbai, Chennai etc.)
4. Your personal favourites

Using this, you can update your entire preference list in less than a minute.

# How to use
1. Git clone
2. `pip install -r requirements` or use conda install
3. Go to [PS Portal](http://psd.bits-pilani.ac.in/Login.aspx) -
    1. Go to [Problem Banks](http://psd.bits-pilani.ac.in/Student/ViewActiveStationProblemBankData.aspx) page -> save as problem_bank.html
    2. Go to [Preferences](http://psd.bits-pilani.ac.in/Student/StudentStationPreference.aspx) page -> save as ps.html
    3. Make sure the downloaded html files are in the same folder as this README file
4. Modify lines 8 to 29 in _main.py_ to adjust your preference.
5. Run `python main.py`

Once you run this, you should get a new file _ps_modified.html_ in your directory. Copy entire list of `li` elements from this file (starts from lin 555), inspect element of your PS portal Preferences page and replace the `li` elements (found inside `ul` with id='sortable_nav'). 

Click on **Save All Preferences** and you are done!
