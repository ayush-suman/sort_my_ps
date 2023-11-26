# How to use
1. Git clone
2. `pip install -r requirements` or use conda install
3. Go to [PS Portal](http://psd.bits-pilani.ac.in/Login.aspx) -
    3.1 Go to [Problem Banks](http://psd.bits-pilani.ac.in/Student/ViewActiveStationProblemBankData.aspx) page -> save as problem_bank.html
    3.2 Go to [Preferences](http://psd.bits-pilani.ac.in/Student/StudentStationPreference.aspx) page -> save as ps.html
    3.3 Make sure the downloaded html files are in the same folder as this README file
4. Modify lines 9 to 21 as per your preference in _main.py_
5. Run `python main.py`

Once you run this, you should get a new file _ps_modified.html_ in your directory. Copy the content of this file, inspect element of your PS portal Preferences page and replace the html code there. Click on *Save All Preferences* and you are done.