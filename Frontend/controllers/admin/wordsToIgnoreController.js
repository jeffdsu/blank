blankApp.controller('adminWordsToIgnoreController', ['$scope', '$resource', '$routeParams', '$http', 'wordsToIgnoreService', function ($scope, $resource, $routeParams, $http, wordsToIgnoreService) {
    
    wordsToIgnoreService.get_collection()
        .then(function (data) {
                console.log("asdf");
                $scope.words_to_ignore = data;
            }
            , function (err) {

            }
        );

}]);