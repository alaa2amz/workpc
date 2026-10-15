fc-list|awk -F\: '{print $2}'|awk -F\, '{print $1}'|awk '{print $0":<br/> <span style=\"color:red;font-size:30pt;font-family:"$0";\" >'$1'</span></br>"}' |tee frag.html
