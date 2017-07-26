/**
 * Created by sun on 7/18/2017.
 */

var alliedApp = angular.module('allied',['ngMaterial','ngMessages']);


//main controller
alliedApp.controller("alliedController",function ($scope,$http) {

            // get func
            $http.get("/api/get")
                .then(function (response) {
                    $scope.posts = response.data;
                });
            // // post func
            //  var data = $.param({
            //     fName: $scope.firstName,
            //     lName: $scope.lastName
            // });
            //
            // var config = {
            //     headers : {ww
            //         'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
            //     }
            // }
            //
            // $http.post('/ServerRequest/PostDataResponse', data, config)
            // .success(function (data, status, headers, config) {
            //     $scope.PostDataResponse = data;
            // })

            /**
             * filter
             */

            //date piocker
              $scope.myDate = "";
              $scope.isOpen = false;


$scope.change = function(selection) {
      console.log(selection);
    if($scope.myStatus=="All"){
        $scope.searchText = "";
        console.log("nihao");

    }
    }

        });


