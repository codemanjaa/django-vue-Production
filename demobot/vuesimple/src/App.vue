<template>
  <div class="container">
    <div class="row">
      <div class="col-3">
        <sidebar-menu :menu="menu"/>
      </div>


      <div class="col-9">

        <router-view/>
        <!--<group-gadget></group-gadget>-->
      </div>
    </div>
    <div class="row">
      <!--<user-profile></user-profile>-->
      <div class="col-4">
      </div>
      <!--<div class="col-8">-->
      <!--<UserProfile></UserProfile>-->
      <!--</div>-->
    </div>
    <div id="nav">
      <!--<router-link to="/groups">Groups</router-link>-->
    </div>

  </div>
</template>

<script>
  import GroupList from './component/GroupList.vue';
  import GroupStat from "./component/GroupStat";
  import GroupGadget from "./component/GroupGadget";
  import UserProfile from "./component/UserProfile"
  import CreateNewGroup from "./component/CreateNewGroup";
  import Logout from './component/Logout'

  export default {

    data() {
      return {
        menu: [
          {
            header: true,
            title: 'Admin Panel - Stop Smoking',
            // component: componentName
            // visibleOnCollapse: true
            // class: ''
            // attributes: {}
          },
          {
            href: '/',
            title: 'Dashboard',
            icon: 'fa fa-user',
            /*
            // custom icon
            icon: {
                element: 'span',
                class: 'fa fa-user',
                attributes: {}
                text: ''
            }
            */
            // disabled: true
            // class: ''
            // attributes: {}
            // alias: '/path'
            /*
            badge: {
                text: 'new',
                class: 'default-badge'
                // attributes: {}
                // element: 'span'
            }
            */
          },
          {
            title: 'Group Management',
            icon: 'fa fa-chart-area',
           // href: '/groups',
           // component: GroupGadget,
            child: [
              {
                title: '--- Group Stats',
                icon: 'fa fa-chart-area',
                href: '/groups',
                component: GroupGadget,
              },
              {
                title: '--- Create New Group',
                href: '/creategroup',
                component: CreateNewGroup,
              }


            ]
          },
          {
            title: 'User Management',
            icon: 'fa fa-chart-area',
            href: '/users',
            component: UserProfile,
            child: []
          },
          {
            title: 'Setting',
            icon: 'fa fa-chart-area',
            child: [
              {
                title: '---    Group Phase Management ',
                icon: 'fa fa-chart-area',
                href: '/groupsetting',

              },


            ]
          },
          {
            title: 'Logout',
            icon: 'fa fa-chart-area',
            href: '/logout',

          }
        ]
      }
    },
    components: {GroupGadget, GroupStat, GroupList, UserProfile, Logout}
  }
</script>
