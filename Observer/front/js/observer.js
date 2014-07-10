angular.module("MyAppObserver", ['ngResource']);

function ObserverCtrl($scope, $resource, $http){

    // static variable
    $http.defaults.headers.put["Content-Type"] = "application/x-www-form-urlencoded";

    $scope.api_url = 'http://api.observer.thebault.co';
    $scope.id_rss = 0;
    $scope.panel_title = 'Observer';
    $scope.rss_cat = new Array('Python', 'Devs', 'Others');
    $scope.feedsFilter = {
        'type': ''
    };
    $scope.info_from_update = null;
    $scope.remaining_feeds = 0;

    // retrieve RSS list
    $scope.rss = $resource("http://api.observer.thebault.co/rss/",
        {callback:'JSON_CALLBACK'},
        {get:{method:'JSONP'}}
    );

    // retrieve FEEDS list
    $scope.feeds = $resource("http://api.observer.thebault.co/feeds/:feedID", {feedID:'@id', callback:'JSON_CALLBACK'},
        {
            get:{method:'JSONP'},
            put:{method:'PUT'}
        });

    // perform AJAX requests
    $scope.rss.get(function(data){
            console.log('<rss_list> request success');
            $scope.rss_list = data['data'];
        }, function(err){
            console.log('<rss_list> request failed: ', err);
        }
    );

    $scope.feeds.get({q: {'status': 'new'}}, function(data){
            console.log('<feeds_list> request success');
            $scope.feeds_list = data['data'];
            $scope.remaining_feeds = data['count'];
        }, function(err){
            console.log('<feeds_list> request failed: ', err);
        }
    );

    $scope.changeFeedsFilter = function(type){
        console.log(type);
        $scope.feedsFilter = {
            'type': type
        };
    };

    $scope.updateFeed = function(feed, update){
        $http({
            method: 'PUT',
            url: 'http://api.observer.thebault.co/feeds/'+feed,
            data: $.param({'status': update})
        }).
        success(function(response) {
            console.log('<'+update+'Feed> request success: ', response['data']);
            $scope.info_from_update = update.toUpperCase()+': '+response['data'][0].title;
            $scope.remaining_feeds -= 1;

            // NOTE: improve this ugly remove wat
            $.each($scope.feeds_list, function(index, result)
            {
                if (result['_id'] === feed)
                {
                    console.log('<findAndRemove> _id found (',index,')');
                    $scope.feeds_list.splice(index, 1);
                }
            });
        }).
        error(function(response) {
            console.log('<'+update+'Feed> request failed: ', response);
        });
    };
}
