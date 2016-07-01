blankApp.controller('mediaController', ['$scope', '$resource', '$routeParams', '$http', '$interval', 'mediaService', 'insightService', '$location', function ($scope, $resource, $routeParams, $http, $interval, mediaService, insightService, $location) {

    var insights_interval;
    $scope.checked = 'I';
    $scope.mediaType = $routeParams.mediaType;
    mediaService.mediaType = $scope.mediaType;

    


    $scope.get_random_insight_for_each_book = function () {

        angular.forEach($scope.books, function (value, key) {
            mediaService.get_random_insight(value.id, $scope.query)
                .then(function (data) {
                    value.insight = data[0];
                }, function (err) {

                })
        });
    };

    $scope.stop_getting_of_insights = function () {
        if (angular.isDefined(insights_interval)) {
            $interval.cancel(insights_interval);
        }
    }

    $scope.go_to_add_medium = function () {
        $location.path($location.path() + '/add').replace();
    };

    mediaService.get_collection()
        .then(function (data) {
                $scope.books = data;
                $scope.get_random_insight_for_each_book();
                if (angular.isDefined(insights_interval)) return;
                insights_interval = $interval($scope.get_random_insight_for_each_book, 5000);

            }
            , function (err) {

            }
        );

    $scope.$on('$destroy', function () {
        $scope.stop_getting_of_insights();
    });
}]);

blankApp.controller('addMediumController', ['$scope', '$resource', '$routeParams', '$http', 'mediaService', 'contributorService', 'mediumTypeService', 'contributionTypeService', function ($scope, $resource, $routeParams, $http, mediaService, contributorService, mediumTypeService, contributionTypeService) {

    $scope.new_medium = Object();
    $scope.new_medium.contributions = [];
    $scope.new_medium.links = [];

    $scope.add_new_medium = function (new_medium) {
        mediaService.create(new_medium);
    };

    contributionTypeService.get_collection()
        .then(function (data) {
            $scope.contribution_types = data;
        }, function (err) {});

    contributorService.get_collection()
        .then(function (data) {
            $scope.contributors = data;
        }, function (err) {});

    mediumTypeService.get_collection()
        .then(function (data) {
            $scope.medium_types = data;
        }, function (err) {});

    $scope.add_medium = function (medium) {
        mediaService.create(medium).then(function (data) {

        }, function (err) {})
    }

    $scope.add_to_contributions = function (new_contribution) {
        $scope.new_medium.contributions.push(angular.copy(new_contribution));
    }

    $scope.add_to_links = function (new_link) {
        $scope.new_medium.links.push(angular.copy(new_link));
    }
    $scope.add_contributor_modal = function () {
        console.log($scope.dialogShown);
        $scope.dialogShown = !$scope.dialogShown;
    }

}]);

blankApp.controller('addContributorController', ['$scope', '$resource', '$routeParams', '$http', 'mediaService', 'contributorService', 'mediumTypeService', 'contributionTypeService', function ($scope, $resource, $routeParams, $http, mediaService, contributorService, mediumTypeService, contributionTypeService) {


    $scope.add_new_contributor = function (contributor) {
        contributorService.create(contributor).then(function (contributor) {
            $scope.contributors.push(contributor);
        }, function (err) {})
    }


}]);

blankApp.controller('indexController', ['$scope', '$resource', '$routeParams', '$http', 'mediaService', 'contributorService', 'mediumTypeService', 'Auth', function ($scope, $resource, $routeParams, $http, mediaService, contributorService, mediumTypeService, Auth) {


   $scope.is_logged_in = function () {
        return Auth.is_logged_in();
    };


}]);




blankApp.controller('inspirationController', ['$scope', '$resource', '$routeParams', '$http', 'mediumTypeService', function ($scope, $resource, $routeParams, $http, mediumTypeService) {


    mediumTypeService.get_collection()
        .then(function (data) {
                $scope.mediums_types = data;
            }
            , function (err) {

            }
        );


}]);

blankApp.controller('navController', ['$scope', '$resource', '$routeParams', '$http', '$location', 'Auth', function ($scope, $resource, $routeParams, $http, $location, Auth) {

    $scope.signout = function () {
        Auth.signout()
            .then(function (data) {
                    $location.path('signin').replace();

                }
                , function (err) {
                    $scope.error = 'Invalid credentials.';
                }
            );
    };

    $scope.is_logged_in = function () {
        return Auth.is_logged_in();
    };


}]);

blankApp.controller('mediaDetailController', ['$scope', '$resource', '$routeParams', '$http', 'mediaService', function ($scope, $resource, $routeParams, $http, mediaService) {


    $scope.mediaType = $routeParams.mediaType;
    mediaService.mediaType = $scope.mediaType;




    mediaService.id = $routeParams.mediaId;


    mediaService.get($routeParams.mediaId)
        .then(function (data) {
            $scope.book = data;
        }, function (err) {

        });

    mediaService.get_insights($routeParams.mediaId)
        .then(function (data) {
            $scope.insights = data;
        }, function (err) {


        });




}]);


blankApp.controller('InsightsComController', ['$scope', '$resource', '$routeParams', '$http', 'mediaService', 'Auth', 'tagService', function ($scope, $resource, $routeParams, $http, mediaService, Auth, tagService) {

    
    $scope.insight = Object();
    $scope.insight.tags = [];
    
    $scope.message = "";
    $scope.dialogShown= {
        value: false
    };
    
    tagService.get_collection()
        .then(function (data) {
            console.log(data);
            $scope.tags = data;
        }, function (err) {


        });
    
    $scope.create_a_new_tag = function (new_tag) {

        tagService.create(new_tag)
            .then(function (data) {
                $scope.tags.push(data);
                $scope.message = "New Tag created";
            })
    }
    
    $scope.add_insight = function (insight) {

        mediaService.add_insight($scope.medium, insight)
            .then(function (data) {
                $scope.insightsList.push(data);
                $scope.message = "Success: Insight has been submitted for validation";
            })
    }

    $scope.add_insight_modal = function () {
        console.log($scope.dialogShown);
        $scope.dialogShown.value = !$scope.dialogShown.value;
    }

    $scope.is_logged_in = function () {
        return Auth.is_logged_in();
    };
    
    $scope.add_to_tags = function (new_tag) {
        $scope.insight.tags.push(angular.copy(new_tag));
        console.log($scope.insight.tags);
    };
    

}]);

blankApp.controller('errorController', ['urls', '$rootScope', '$scope', '$resource', '$routeParams', '$http', '$localStorage', '$location', 'errorService', function (urls, $rootScope, $scope, $resource, $routeParams, $http, $localStorage, $location, errorService) {


    $scope.error = errorService.error;

    $scope.$watch('errorService.error', function (newVal, oldVal, scope) {
        console.log(newVal);
    }, true);

}]);


blankApp.controller('authController', ['urls', '$rootScope', '$scope', '$resource', '$routeParams', '$http', '$localStorage', '$location', 'Auth', 'errorService', function (urls, $rootScope, $scope, $resource, $routeParams, $http, $localStorage, $location, Auth, errorService) {


    $scope.$watch('$scope.message', function (newVal, oldVal, scope) {
        console.log(newVal);
    }, true);

    $scope.signin = function () {

        var formData = {
            username: $scope.username
            , password: $scope.password
        };

        Auth.signin(formData)
            .then(function (data) {
                    $localStorage.token = data.key;
                    $location.path('inspiration-corner').replace();

                }
                , function (err) {
                    $scope.error = 'Invalid credentials.';
                }
            );

    };

    $scope.signup = function () {


        Auth.signup($scope.user_signup)
            .then(function (data) {
                    $scope.message = "Sign Up Successful"

                }
                , function (err) {
                    $scope.error = err;
                }
            );
    };




}]);