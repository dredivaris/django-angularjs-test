/**
* Register controller
* @namespace thinkster.authentication.controllers
*/
(function (){
  'use strict';

  angular
      .module('thinkster.authentication.controllers')
      .controller('RegisterController', RegisterController);

  /**
  * @namespace RegisterController
  */
  function RegisterController($location, $scope, Authentication) {
    var vm = this;

    vm.register = register;

    /**
    * @name register
    * @desc Register a new user
    * @memberOf thinkster.authentication.controllers.RegisterController
    */
    function register() {
      Authentication.register(vm.email, vm.first_name, vm.last_name, vm.password, vm.username);
    }
  }
})();