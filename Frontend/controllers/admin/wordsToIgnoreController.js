blankApp.controller('adminWordsToIgnoreController', ['$scope', '$resource', '$routeParams', '$http', 'wordsToIgnoreService', function ($scope, $resource, $routeParams, $http, wordsToIgnoreService) {
    
    $scope.words_to_ignore = [];
    
    wordsToIgnoreService.get_collection()
        .then(function (data) {
                $scope.words_to_ignore = data;
            }
            , function (err) {

            }
        );

    $scope.add_word_to_ignore = function () {
        wordsToIgnoreService.create($scope.word_to_add)
        .then(function(data){
            $scope.words_to_ignore.append(data);
        }, function(err){});
    };
}]);