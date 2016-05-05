blankApp.filter('authorFilter', function () {
    return function (author) {
        temp_str = "<a href='#/inspiration/authors/" + author.id + "'>" + author.first_name + " ";
        if (author.middle_initial) {
            temp_str += author.middle_initial + " "
        }
        temp_str += author.last_name + "</a>";
        return temp_str;
    };
});


blankApp.filter('insightColorFilter', function () {
    return function (insight, keywords) {
        if (insight && keywords) {
            temp_arr = insight.lesson.split(" ");
            temp_str = "";
            for (i = 0; i < temp_arr.length; i++) {
                var myRegexp = /(\w+)/g;
                var match = myRegexp.exec(temp_arr[i]);
                if (match && match[1] in keywords) {
                    var res = temp_arr[i].replace(match[1], '<span class="impacted_word_' + keywords[match[1]][0] + '">' + match[1] + '</span>');
                    console.log(res);
                    temp_str += res + " ";
                } else {
                    temp_str += temp_arr[i] + " ";
                }
            }
            return temp_str;
        }
        return "";
    };
});


blankApp.filter('insightLinkToUserFilter', function () {
    return function (insight) {
        if (insight) {
            return "<a href='#/inspiration/users/" + insight.user + "'>" + insight.lesson + "</a>";
        }
        return "";
    };
});