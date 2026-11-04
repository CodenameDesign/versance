// Replays the captured interaction states in the static replica: menus, dropdowns, calendars, dialogs, tooltips.
// The recorded popup markup is inserted where it appeared in the original, with the recorded enter/exit motion.
(function () {
  'use strict';
  var STATES = [{"id":"s1","parent":null,"kind":"listbox","trigger":{"id":"1060","action":"click","docRect":[578,5600.63,555,39]},"changes":[{"id":"266","name":"style","old":"top: 109px; min-width: 113px; left: 837px; margin-top: 0px;","new":null},{"id":"259","name":"class","old":"itemDepth02233374943__root itemDepth02233374943--isHovered StylableHorizontalMenu3372578893__menuItem itemShared2352141355__menuItem","new":"itemDepth02233374943__root StylableHorizontalMenu3372578893__menuItem itemShared2352141355__menuItem"},{"id":"259","name":"aria-expanded","old":"true","new":"false"},{"id":"257","name":"data-hovered","old":"true","new":null},{"id":"257","name":"data-shown","old":"true","new":null},{"id":"263","name":"class","old":"itemShared2352141355__accessibilityIcon itemShared2352141355--isOpen","new":"itemShared2352141355__accessibilityIcon"},{"id":"1060","name":"class","old":"sqaxP2l sPAw12I sKv4tNB ojaRfgA--fullWidth ojaRfgA---paddingMode-15-dynamicPaddings ojaRfgA---hoverStyle-9-underline s__9XlkfT o_uTWgF--placeholder o_uTWgF--upgrade s_6zHcA seJ4A_h","new":"sqaxP2l sPAw12I oeSO0I_--focus sKv4tNB ojaRfgA--fullWidth ojaRfgA---paddingMode-15-dynamicPaddings ojaRfgA---hoverStyle-9-underline s__9XlkfT o_uTWgF--placeholder o_uTWgF--upgrade s_6zHcA seJ4A_h"},{"id":"1060","name":"data-focusable-focus","old":"false","new":"true"},{"id":"1060","name":"aria-expanded","old":"false","new":"true"},{"id":"1058","name":"class","old":"sF_7EKY sp78Ud0 sLQP7YS oMMt3sv---alignment-6-bottom oMMt3sv---theme-3-box swTHtDn","new":"sF_7EKY sp78Ud0 oop7Odd--content-visible sLQP7YS oMMt3sv---alignment-6-bottom oMMt3sv---theme-3-box swTHtDn"},{"id":"170","name":"class","old":"uZIV9d","new":"uZIV9d Q0rcTZ"},{"id":"1102","name":"class","old":"uZIV9d","new":"uZIV9d Q0rcTZ"}],"roots":[{"id":"s1-0-0","existing":false,"html":"<div data-hook=\"popover-content\" data-content-element=\"popover-content-core-dropdown-undefined\" data-placement=\"bottom\" class=\"sPnSOOu clickOutside957 seiUj0z sVF1lqp\" style=\"position: absolute; z-index: 1000; will-change: transform; top: 0px; left: 0px; transform: translate3d(-1px, 39px, 0px);\" data-pc-i=\"s1-0-0\"><div class=\"\" data-pc-i=\"s1-0-1\"><div class=\"scVjYHl sbmPLQf\" data-hook=\"dropdown-content\" data-pc-i=\"s1-0-2\"><div role=\"listbox\" class=\"s_yoax0\" id=\"dropdown-options-container_-9\" tabindex=\"-1\" data-hook=\"dropdown-content-options-container\" data-pc-i=\"s1-0-3\"><div id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-0\" tabindex=\"-1\" class=\"sMH81nU otzPKtS--selectable slLM3OI\" aria-labelledby=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-0-text\" data-hook=\"dropdown-content-option\" role=\"option\" aria-disabled=\"false\" aria-selected=\"false\" title=\"Public Relations\" data-pc-i=\"s1-0-4\"><div data-hook=\"dropdown-option\" class=\"sFLbgqe oYk31qI--selectable oYk31qI---textOverflow-8-ellipsis sP8lP2I\" data-pc-i=\"s1-0-5\"><div class=\"sAQ_vfZ\" data-pc-i=\"s1-0-6\"><span class=\"sf4zzLJ o__22sN2C---typography-11-runningText o__22sN2C---priority-7-primary sFzt5ak\" aria-hidden=\"false\" id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-0-text\" aria-disabled=\"false\" data-pc-i=\"s1-0-7\">Public Relations</span></div></div></div><div id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-1\" tabindex=\"-1\" class=\"sMH81nU otzPKtS--selectable slLM3OI\" aria-labelledby=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-1-text\" data-hook=\"dropdown-content-option\" role=\"option\" aria-disabled=\"false\" aria-selected=\"false\" title=\"Marketing\" data-pc-i=\"s1-0-8\"><div data-hook=\"dropdown-option\" class=\"sFLbgqe oYk31qI--selectable oYk31qI---textOverflow-8-ellipsis sP8lP2I\" data-pc-i=\"s1-0-9\"><div class=\"sAQ_vfZ\" data-pc-i=\"s1-0-10\"><span class=\"sf4zzLJ o__22sN2C---typography-11-runningText o__22sN2C---priority-7-primary sFzt5ak\" aria-hidden=\"false\" id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-1-text\" aria-disabled=\"false\" data-pc-i=\"s1-0-11\">Marketing</span></div></div></div><div id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-2\" tabindex=\"-1\" class=\"sMH81nU otzPKtS--selectable slLM3OI\" aria-labelledby=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-2-text\" data-hook=\"dropdown-content-option\" role=\"option\" aria-disabled=\"false\" aria-selected=\"false\" title=\"Legal\" data-pc-i=\"s1-0-12\"><div data-hook=\"dropdown-option\" class=\"sFLbgqe oYk31qI--selectable oYk31qI---textOverflow-8-ellipsis sP8lP2I\" data-pc-i=\"s1-0-13\"><div class=\"sAQ_vfZ\" data-pc-i=\"s1-0-14\"><span class=\"sf4zzLJ o__22sN2C---typography-11-runningText o__22sN2C---priority-7-primary sFzt5ak\" aria-hidden=\"false\" id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-2-text\" aria-disabled=\"false\" data-pc-i=\"s1-0-15\">Legal</span></div></div></div><div id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-3\" tabindex=\"-1\" class=\"sMH81nU otzPKtS--selectable slLM3OI\" aria-labelledby=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-3-text\" data-hook=\"dropdown-content-option\" role=\"option\" aria-disabled=\"false\" aria-selected=\"false\" title=\"Investor Relations\" data-pc-i=\"s1-0-16\"><div data-hook=\"dropdown-option\" class=\"sFLbgqe oYk31qI--selectable oYk31qI---textOverflow-8-ellipsis sP8lP2I\" data-pc-i=\"s1-0-17\"><div class=\"sAQ_vfZ\" data-pc-i=\"s1-0-18\"><span class=\"sf4zzLJ o__22sN2C---typography-11-runningText o__22sN2C---priority-7-primary sFzt5ak\" aria-hidden=\"false\" id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-3-text\" aria-disabled=\"false\" data-pc-i=\"s1-0-19\">Investor Relations</span></div></div></div><div id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-4\" tabindex=\"-1\" class=\"sMH81nU otzPKtS--selectable slLM3OI\" aria-labelledby=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-4-text\" data-hook=\"dropdown-content-option\" role=\"option\" aria-disabled=\"false\" aria-selected=\"false\" title=\"Finance\" data-pc-i=\"s1-0-20\"><div data-hook=\"dropdown-option\" class=\"sFLbgqe oYk31qI--selectable oYk31qI---textOverflow-8-ellipsis sP8lP2I\" data-pc-i=\"s1-0-21\"><div class=\"sAQ_vfZ\" data-pc-i=\"s1-0-22\"><span class=\"sf4zzLJ o__22sN2C---typography-11-runningText o__22sN2C---priority-7-primary sFzt5ak\" aria-hidden=\"false\" id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-4-text\" aria-disabled=\"false\" data-pc-i=\"s1-0-23\">Finance</span></div></div></div><div id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-5\" tabindex=\"-1\" class=\"sMH81nU otzPKtS--selectable slLM3OI\" aria-labelledby=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-5-text\" data-hook=\"dropdown-content-option\" role=\"option\" aria-disabled=\"false\" aria-selected=\"false\" title=\"Communications\" data-pc-i=\"s1-0-24\"><div data-hook=\"dropdown-option\" class=\"sFLbgqe oYk31qI--selectable oYk31qI---textOverflow-8-ellipsis sP8lP2I\" data-pc-i=\"s1-0-25\"><div class=\"sAQ_vfZ\" data-pc-i=\"s1-0-26\"><span class=\"sf4zzLJ o__22sN2C---typography-11-runningText o__22sN2C---priority-7-primary sFzt5ak\" aria-hidden=\"false\" id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-5-text\" aria-disabled=\"false\" data-pc-i=\"s1-0-27\">Communications</span></div></div></div><div id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-6\" tabindex=\"-1\" class=\"sMH81nU otzPKtS--selectable slLM3OI\" aria-labelledby=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-6-text\" data-hook=\"dropdown-content-option\" role=\"option\" aria-disabled=\"false\" aria-selected=\"false\" title=\"CEO\" data-pc-i=\"s1-0-28\"><div data-hook=\"dropdown-option\" class=\"sFLbgqe oYk31qI--selectable oYk31qI---textOverflow-8-ellipsis sP8lP2I\" data-pc-i=\"s1-0-29\"><div class=\"sAQ_vfZ\" data-pc-i=\"s1-0-30\"><span class=\"sf4zzLJ o__22sN2C---typography-11-runningText o__22sN2C---priority-7-primary sFzt5ak\" aria-hidden=\"false\" id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-6-text\" aria-disabled=\"false\" data-pc-i=\"s1-0-31\">CEO</span></div></div></div><div id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-7\" tabindex=\"-1\" class=\"sMH81nU otzPKtS--selectable slLM3OI\" aria-labelledby=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-7-text\" data-hook=\"dropdown-content-option\" role=\"option\" aria-disabled=\"false\" aria-selected=\"false\" title=\"Board Member\" data-pc-i=\"s1-0-32\"><div data-hook=\"dropdown-option\" class=\"sFLbgqe oYk31qI--selectable oYk31qI---textOverflow-8-ellipsis sP8lP2I\" data-pc-i=\"s1-0-33\"><div class=\"sAQ_vfZ\" data-pc-i=\"s1-0-34\"><span class=\"sf4zzLJ o__22sN2C---typography-11-runningText o__22sN2C---priority-7-primary sFzt5ak\" aria-hidden=\"false\" id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-7-text\" aria-disabled=\"false\" data-pc-i=\"s1-0-35\">Board Member</span></div></div></div><div id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-8\" tabindex=\"-1\" class=\"sMH81nU otzPKtS--selectable slLM3OI\" aria-labelledby=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-8-text\" data-hook=\"dropdown-content-option\" role=\"option\" aria-disabled=\"false\" aria-selected=\"false\" title=\"Other\" data-pc-i=\"s1-0-36\"><div data-hook=\"dropdown-option\" class=\"sFLbgqe oYk31qI--selectable oYk31qI---textOverflow-8-ellipsis sP8lP2I\" data-pc-i=\"s1-0-37\"><div class=\"sAQ_vfZ\" data-pc-i=\"s1-0-38\"><span class=\"sf4zzLJ o__22sN2C---typography-11-runningText o__22sN2C---priority-7-primary sFzt5ak\" aria-hidden=\"false\" id=\"dropdown-options-container_-9_option-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-opt-8-text\" aria-disabled=\"false\" data-pc-i=\"s1-0-39\">Other</span></div></div></div></div></div></div></div>","parentId":"1058","beforeId":null,"position":"absolute"}],"timing":{"appearMs":7.1,"settleMs":52.6,"exitMs":12.2},"animations":[],"closeAnimations":[],"startSamples":[{"opacity":"0","transform":"none","visibility":"visible"}],"endSamples":[{"opacity":"1","transform":"matrix(1, 0, 0, 1, -1, 39)","visibility":"visible"}]},{"id":"s2","parent":null,"kind":"dialog","trigger":{"id":"1293","action":"click","docRect":[1162.34,6017.63,235.66,36.38]},"changes":[{"id":"1060","name":"class","old":"sqaxP2l sPAw12I oeSO0I_--focus oeSO0I_--focus-visible sKv4tNB ojaRfgA--fullWidth ojaRfgA---paddingMode-15-dynamicPaddings ojaRfgA---hoverStyle-9-underline s__9XlkfT o_uTWgF--placeholder o_uTWgF--upgrade s_6zHcA seJ4A_h","new":"sqaxP2l sPAw12I sKv4tNB ojaRfgA--fullWidth ojaRfgA---paddingMode-15-dynamicPaddings ojaRfgA---hoverStyle-9-underline s__9XlkfT o_uTWgF--error o_uTWgF--placeholder o_uTWgF--upgrade s_6zHcA seJ4A_h"},{"id":"1060","name":"data-focusable-focus","old":"true","new":"false"},{"id":"1060","name":"data-focusable-focus-visible","old":"true","new":"false"},{"id":"1060","name":"data-dropdown-base-error","old":"false","new":"true"},{"id":"1060","name":"aria-describedby","old":null,"new":"form-field-error-14b2f38d-b2b7-4b57-0ee8-038ed2e3741d-comp-mpx2oh16-"},{"id":"1060","name":"aria-invalid","old":"false","new":"true"},{"id":"1056","name":"class","old":"slP6sMf oeM_EMx---errorAppearance-8-TextOnly sLQP7YS oMMt3sv---alignment-6-bottom oMMt3sv---theme-3-box oMMt3sv--newErrorMessage s_mowPn scwMXAj s__6VqN23","new":"slP6sMf oeM_EMx---errorAppearance-8-TextOnly sLQP7YS oMMt3sv---alignment-6-bottom oMMt3sv---theme-3-box oMMt3sv--newErrorMessage oMMt3sv--error s_mowPn scwMXAj s__6VqN23 undefined"},{"id":"1066","name":"class","old":"slP6sMf oeM_EMx---errorAppearance-8-TextOnly s__0oqQvY","new":"slP6sMf oeM_EMx--visible oeM_EMx---errorAppearance-8-TextOnly s__0oqQvY"}],"roots":[{"id":"s2-0-0","existing":false,"html":"<div class=\"IjodFk\" data-hook=\"consent-banner-settings-container\" data-comp-type=\"cookie-banner-modal-uou\" tabindex=\"-1\" aria-labelledby=\"settings.title.id\" role=\"dialog\" data-pc-i=\"s2-0-0\"><div class=\"f1uNCG\" data-pc-i=\"s2-0-1\"></div><section class=\"O_5igK\" data-hook=\"consent-banner-settings-dialog\" data-pc-i=\"s2-0-2\"><h2 class=\"xeX9T7\" id=\"settings.title.id\" data-pc-i=\"s2-0-3\">Advanced Cookie Settings</h2><span class=\"THrZzf\" data-pc-i=\"s2-0-4\"><button class=\"A9d5ZY \" aria-label=\"Close Settings\" data-pc-i=\"s2-0-5\"><img class=\"EiWNMp \" alt=\"Close Settings\" src=\"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij48Zz48Zz48Zz48cGF0aCBmaWxsPSIjMDAwIiBpZD0iY2xvc2Utc3ZnLXBhdGgiIGQ9Ik0xNy4yOTQgNmwuNzA2LjcwNkwxMi43MDUgMTIgMTggMTcuMjk0bC0uNzA2LjcwNkwxMiAxMi43MDUgNi43MDYgMTggNiAxNy4yOTQgMTEuMjk1IDEyIDYgNi43MDYgNi43MDYgNiAxMiAxMS4yOTUgMTcuMjk0IDZ6IiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNDcxLjAwMDAwMCwgLTY0Ni4wMDAwMDApIHRyYW5zbGF0ZSg0NzEuMDAwMDAwLCA2NDYuMDAwMDAwKSIvPjwvZz48L2c+PC9nPjwvc3ZnPg==\" data-pc-i=\"s2-0-6\"></button></span><section class=\"Crda13\" data-pc-i=\"s2-0-7\"><section class=\"jKUVL1\" data-hook=\"consent-banner-section-root\" data-pc-i=\"s2-0-8\"><h3 class=\"HXQaTB\" id=\"policy.banner.id_1_nuldhprfrp\" data-hook=\"consent-banner-section-title\" data-pc-i=\"s2-0-9\">Essential Cookies</h3><p class=\"sKz7eY\" id=\"policy.banner.id_2_abdlwju\" data-hook=\"consent-banner-section-description\" data-pc-i=\"s2-0-10\">These cookies enable core functionality such as security, verification of identity and network management. These cookies can’t be disabled.</p><span data-hook=\"consent-banner-section-toggle\" class=\"dz8xDz _a6Ccw\" data-pc-i=\"s2-0-11\"><input class=\"BfPLBO\" id=\"consent-banner-toggleEnabled-input-id_0\" data-hook=\"consent-banner-section-toggle-input\" aria-labelledby=\"policy.banner.id_1_nuldhprfrp\" aria-describedby=\"policy.banner.id_2_abdlwju\" type=\"checkbox\" disabled=\"\" data-pc-i=\"s2-0-12\"><label class=\"kCHabv\" for=\"consent-banner-toggleEnabled-input-id_0\" data-pc-i=\"s2-0-13\"><span class=\"NDtop7\" data-pc-i=\"s2-0-14\"></span><span class=\"MezgNL\" data-pc-i=\"s2-0-15\"><svg class=\"tXvr8R n97qfL\" viewBox=\"0 0 11 2\" fill=\"currentColor\" width=\"10\" height=\"2\" data-pc-i=\"s2-0-16\">\n    <path d=\"M0 0H10V2H0z\" data-pc-i=\"s2-0-17\"></path>\n      </svg><svg class=\"tXvr8R Kdinlh\" viewBox=\"0 0 11 8\" fill=\"currentColor\" width=\"10\" height=\"8\" data-pc-i=\"s2-0-18\">\n        <path d=\"M3.8 5L1.2 2.5 0 3.7 3.8 7.5 10 1.2 8.8 0z\" data-pc-i=\"s2-0-19\"></path>\n      </svg></span></label></span></section><section class=\"jKUVL1\" data-hook=\"consent-banner-section-root\" data-pc-i=\"s2-0-20\"><h3 class=\"HXQaTB\" id=\"policy.banner.id_3_ldkpazfsn\" data-hook=\"consent-banner-section-title\" data-pc-i=\"s2-0-21\">Enable Marketing Cookies</h3><p class=\"sKz7eY\" id=\"policy.banner.id_4_ztklxxmj\" data-hook=\"consent-banner-section-description\" data-pc-i=\"s2-0-22\">These cookies are used to track advertising effectiveness to provide a more relevant service and deliver better ads to suit your interests.</p><span data-hook=\"consent-banner-section-toggle\" class=\"dz8xDz _a6Ccw\" data-pc-i=\"s2-0-23\"><input class=\"BfPLBO\" id=\"consent-banner-toggleEnabled-input-id_1\" data-hook=\"consent-banner-section-toggle-input\" aria-labelledby=\"policy.banner.id_3_ldkpazfsn\" aria-describedby=\"policy.banner.id_4_ztklxxmj\" type=\"checkbox\" data-pc-i=\"s2-0-24\"><label class=\"kCHabv\" for=\"consent-banner-toggleEnabled-input-id_1\" data-pc-i=\"s2-0-25\"><span class=\"NDtop7\" data-pc-i=\"s2-0-26\"></span><span class=\"MezgNL\" data-pc-i=\"s2-0-27\"><svg class=\"tXvr8R n97qfL\" viewBox=\"0 0 11 2\" fill=\"currentColor\" width=\"10\" height=\"2\" data-pc-i=\"s2-0-28\">\n    <path d=\"M0 0H10V2H0z\" data-pc-i=\"s2-0-29\"></path>\n      </svg><svg class=\"tXvr8R Kdinlh\" viewBox=\"0 0 11 8\" fill=\"currentColor\" width=\"10\" height=\"8\" data-pc-i=\"s2-0-30\">\n        <path d=\"M3.8 5L1.2 2.5 0 3.7 3.8 7.5 10 1.2 8.8 0z\" data-pc-i=\"s2-0-31\"></path>\n      </svg></span></label></span></section><section class=\"jKUVL1\" data-hook=\"consent-banner-section-root\" data-pc-i=\"s2-0-32\"><h3 class=\"HXQaTB\" id=\"policy.banner.id_5_uabnufx\" data-hook=\"consent-banner-section-title\" data-pc-i=\"s2-0-33\">Enable Functional Cookies</h3><p class=\"sKz7eY\" id=\"policy.banner.id_6_kfehwgtqm\" data-hook=\"consent-banner-section-description\" data-pc-i=\"s2-0-34\">These cookies collect data to remember choices users make to improve and give a more personalised experience. </p><span data-hook=\"consent-banner-section-toggle\" class=\"dz8xDz _a6Ccw\" data-pc-i=\"s2-0-35\"><input class=\"BfPLBO\" id=\"consent-banner-toggleEnabled-input-id_2\" data-hook=\"consent-banner-section-toggle-input\" aria-labelledby=\"policy.banner.id_5_uabnufx\" aria-describedby=\"policy.banner.id_6_kfehwgtqm\" type=\"checkbox\" data-pc-i=\"s2-0-36\"><label class=\"kCHabv\" for=\"consent-banner-toggleEnabled-input-id_2\" data-pc-i=\"s2-0-37\"><span class=\"NDtop7\" data-pc-i=\"s2-0-38\"></span><span class=\"MezgNL\" data-pc-i=\"s2-0-39\"><svg class=\"tXvr8R n97qfL\" viewBox=\"0 0 11 2\" fill=\"currentColor\" width=\"10\" height=\"2\" data-pc-i=\"s2-0-40\">\n    <path d=\"M0 0H10V2H0z\" data-pc-i=\"s2-0-41\"></path>\n      </svg><svg class=\"tXvr8R Kdinlh\" viewBox=\"0 0 11 8\" fill=\"currentColor\" width=\"10\" height=\"8\" data-pc-i=\"s2-0-42\">\n        <path d=\"M3.8 5L1.2 2.5 0 3.7 3.8 7.5 10 1.2 8.8 0z\" data-pc-i=\"s2-0-43\"></path>\n      </svg></span></label></span></section><section class=\"jKUVL1\" data-hook=\"consent-banner-section-root\" data-pc-i=\"s2-0-44\"><h3 class=\"HXQaTB\" id=\"policy.banner.id_7_vyonldek\" data-hook=\"consent-banner-section-title\" data-pc-i=\"s2-0-45\">Enable Analytics Cookies</h3><p class=\"sKz7eY\" id=\"policy.banner.id_8_yxiceyd\" data-hook=\"consent-banner-section-description\" data-pc-i=\"s2-0-46\">These cookies help us to understand how visitors interact with our website, discover errors and provide a better overall analytics.</p><span data-hook=\"consent-banner-section-toggle\" class=\"dz8xDz _a6Ccw\" data-pc-i=\"s2-0-47\"><input class=\"BfPLBO\" id=\"consent-banner-toggleEnabled-input-id_3\" data-hook=\"consent-banner-section-toggle-input\" aria-labelledby=\"policy.banner.id_7_vyonldek\" aria-describedby=\"policy.banner.id_8_yxiceyd\" type=\"checkbox\" data-pc-i=\"s2-0-48\"><label class=\"kCHabv\" for=\"consent-banner-toggleEnabled-input-id_3\" data-pc-i=\"s2-0-49\"><span class=\"NDtop7\" data-pc-i=\"s2-0-50\"></span><span class=\"MezgNL\" data-pc-i=\"s2-0-51\"><svg class=\"tXvr8R n97qfL\" viewBox=\"0 0 11 2\" fill=\"currentColor\" width=\"10\" height=\"2\" data-pc-i=\"s2-0-52\">\n    <path d=\"M0 0H10V2H0z\" data-pc-i=\"s2-0-53\"></path>\n      </svg><svg class=\"tXvr8R Kdinlh\" viewBox=\"0 0 11 8\" fill=\"currentColor\" width=\"10\" height=\"8\" data-pc-i=\"s2-0-54\">\n        <path d=\"M3.8 5L1.2 2.5 0 3.7 3.8 7.5 10 1.2 8.8 0z\" data-pc-i=\"s2-0-55\"></path>\n      </svg></span></label></span></section></section><div class=\"lCXq42\" data-pc-i=\"s2-0-56\"><button data-hook=\"consent-banner-settings-save-button\" class=\"YaqqQl Pg7AcP dukD6Z \" data-pc-i=\"s2-0-57\">Save</button></div></section></div>","parentId":"142","beforeId":null,"position":"fixed"}],"timing":{"appearMs":6.1,"settleMs":47.9,"exitMs":12.8},"animations":[],"closeAnimations":[],"startSamples":[{"opacity":"1","transform":"none","visibility":"visible"}],"endSamples":[{"opacity":"1","transform":"none","visibility":"visible"}]},{"id":"s3","parent":null,"kind":"dialog","trigger":{"id":"1294","action":"click","docRect":[1168.34,6019.81,133.31,32]},"changes":[],"roots":[{"id":"s3-0-0","existing":false,"html":"<div class=\"IjodFk\" data-hook=\"consent-banner-settings-container\" data-comp-type=\"cookie-banner-modal-uou\" tabindex=\"-1\" aria-labelledby=\"settings.title.id\" role=\"dialog\" data-pc-i=\"s3-0-0\"><div class=\"f1uNCG\" data-pc-i=\"s3-0-1\"></div><section class=\"O_5igK\" data-hook=\"consent-banner-settings-dialog\" data-pc-i=\"s3-0-2\"><h2 class=\"xeX9T7\" id=\"settings.title.id\" data-pc-i=\"s3-0-3\">Advanced Cookie Settings</h2><span class=\"THrZzf\" data-pc-i=\"s3-0-4\"><button class=\"A9d5ZY \" aria-label=\"Close Settings\" data-pc-i=\"s3-0-5\"><img class=\"EiWNMp \" alt=\"Close Settings\" src=\"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij48Zz48Zz48Zz48cGF0aCBmaWxsPSIjMDAwIiBpZD0iY2xvc2Utc3ZnLXBhdGgiIGQ9Ik0xNy4yOTQgNmwuNzA2LjcwNkwxMi43MDUgMTIgMTggMTcuMjk0bC0uNzA2LjcwNkwxMiAxMi43MDUgNi43MDYgMTggNiAxNy4yOTQgMTEuMjk1IDEyIDYgNi43MDYgNi43MDYgNiAxMiAxMS4yOTUgMTcuMjk0IDZ6IiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNDcxLjAwMDAwMCwgLTY0Ni4wMDAwMDApIHRyYW5zbGF0ZSg0NzEuMDAwMDAwLCA2NDYuMDAwMDAwKSIvPjwvZz48L2c+PC9nPjwvc3ZnPg==\" data-pc-i=\"s3-0-6\"></button></span><section class=\"Crda13\" data-pc-i=\"s3-0-7\"><section class=\"jKUVL1\" data-hook=\"consent-banner-section-root\" data-pc-i=\"s3-0-8\"><h3 class=\"HXQaTB\" id=\"policy.banner.id_9_urpynjzvk\" data-hook=\"consent-banner-section-title\" data-pc-i=\"s3-0-9\">Essential Cookies</h3><p class=\"sKz7eY\" id=\"policy.banner.id_10_bacszxdl\" data-hook=\"consent-banner-section-description\" data-pc-i=\"s3-0-10\">These cookies enable core functionality such as security, verification of identity and network management. These cookies can’t be disabled.</p><span data-hook=\"consent-banner-section-toggle\" class=\"dz8xDz _a6Ccw\" data-pc-i=\"s3-0-11\"><input class=\"BfPLBO\" id=\"consent-banner-toggleEnabled-input-id_4\" data-hook=\"consent-banner-section-toggle-input\" aria-labelledby=\"policy.banner.id_9_urpynjzvk\" aria-describedby=\"policy.banner.id_10_bacszxdl\" type=\"checkbox\" disabled=\"\" data-pc-i=\"s3-0-12\"><label class=\"kCHabv\" for=\"consent-banner-toggleEnabled-input-id_4\" data-pc-i=\"s3-0-13\"><span class=\"NDtop7\" data-pc-i=\"s3-0-14\"></span><span class=\"MezgNL\" data-pc-i=\"s3-0-15\"><svg class=\"tXvr8R n97qfL\" viewBox=\"0 0 11 2\" fill=\"currentColor\" width=\"10\" height=\"2\" data-pc-i=\"s3-0-16\">\n    <path d=\"M0 0H10V2H0z\" data-pc-i=\"s3-0-17\"></path>\n      </svg><svg class=\"tXvr8R Kdinlh\" viewBox=\"0 0 11 8\" fill=\"currentColor\" width=\"10\" height=\"8\" data-pc-i=\"s3-0-18\">\n        <path d=\"M3.8 5L1.2 2.5 0 3.7 3.8 7.5 10 1.2 8.8 0z\" data-pc-i=\"s3-0-19\"></path>\n      </svg></span></label></span></section><section class=\"jKUVL1\" data-hook=\"consent-banner-section-root\" data-pc-i=\"s3-0-20\"><h3 class=\"HXQaTB\" id=\"policy.banner.id_11_grrszkf\" data-hook=\"consent-banner-section-title\" data-pc-i=\"s3-0-21\">Enable Marketing Cookies</h3><p class=\"sKz7eY\" id=\"policy.banner.id_12_lfhqqdwum\" data-hook=\"consent-banner-section-description\" data-pc-i=\"s3-0-22\">These cookies are used to track advertising effectiveness to provide a more relevant service and deliver better ads to suit your interests.</p><span data-hook=\"consent-banner-section-toggle\" class=\"dz8xDz _a6Ccw\" data-pc-i=\"s3-0-23\"><input class=\"BfPLBO\" id=\"consent-banner-toggleEnabled-input-id_5\" data-hook=\"consent-banner-section-toggle-input\" aria-labelledby=\"policy.banner.id_11_grrszkf\" aria-describedby=\"policy.banner.id_12_lfhqqdwum\" type=\"checkbox\" data-pc-i=\"s3-0-24\"><label class=\"kCHabv\" for=\"consent-banner-toggleEnabled-input-id_5\" data-pc-i=\"s3-0-25\"><span class=\"NDtop7\" data-pc-i=\"s3-0-26\"></span><span class=\"MezgNL\" data-pc-i=\"s3-0-27\"><svg class=\"tXvr8R n97qfL\" viewBox=\"0 0 11 2\" fill=\"currentColor\" width=\"10\" height=\"2\" data-pc-i=\"s3-0-28\">\n    <path d=\"M0 0H10V2H0z\" data-pc-i=\"s3-0-29\"></path>\n      </svg><svg class=\"tXvr8R Kdinlh\" viewBox=\"0 0 11 8\" fill=\"currentColor\" width=\"10\" height=\"8\" data-pc-i=\"s3-0-30\">\n        <path d=\"M3.8 5L1.2 2.5 0 3.7 3.8 7.5 10 1.2 8.8 0z\" data-pc-i=\"s3-0-31\"></path>\n      </svg></span></label></span></section><section class=\"jKUVL1\" data-hook=\"consent-banner-section-root\" data-pc-i=\"s3-0-32\"><h3 class=\"HXQaTB\" id=\"policy.banner.id_13_xjjreibb\" data-hook=\"consent-banner-section-title\" data-pc-i=\"s3-0-33\">Enable Functional Cookies</h3><p class=\"sKz7eY\" id=\"policy.banner.id_14_dhfqsleuf\" data-hook=\"consent-banner-section-description\" data-pc-i=\"s3-0-34\">These cookies collect data to remember choices users make to improve and give a more personalised experience. </p><span data-hook=\"consent-banner-section-toggle\" class=\"dz8xDz _a6Ccw\" data-pc-i=\"s3-0-35\"><input class=\"BfPLBO\" id=\"consent-banner-toggleEnabled-input-id_6\" data-hook=\"consent-banner-section-toggle-input\" aria-labelledby=\"policy.banner.id_13_xjjreibb\" aria-describedby=\"policy.banner.id_14_dhfqsleuf\" type=\"checkbox\" data-pc-i=\"s3-0-36\"><label class=\"kCHabv\" for=\"consent-banner-toggleEnabled-input-id_6\" data-pc-i=\"s3-0-37\"><span class=\"NDtop7\" data-pc-i=\"s3-0-38\"></span><span class=\"MezgNL\" data-pc-i=\"s3-0-39\"><svg class=\"tXvr8R n97qfL\" viewBox=\"0 0 11 2\" fill=\"currentColor\" width=\"10\" height=\"2\" data-pc-i=\"s3-0-40\">\n    <path d=\"M0 0H10V2H0z\" data-pc-i=\"s3-0-41\"></path>\n      </svg><svg class=\"tXvr8R Kdinlh\" viewBox=\"0 0 11 8\" fill=\"currentColor\" width=\"10\" height=\"8\" data-pc-i=\"s3-0-42\">\n        <path d=\"M3.8 5L1.2 2.5 0 3.7 3.8 7.5 10 1.2 8.8 0z\" data-pc-i=\"s3-0-43\"></path>\n      </svg></span></label></span></section><section class=\"jKUVL1\" data-hook=\"consent-banner-section-root\" data-pc-i=\"s3-0-44\"><h3 class=\"HXQaTB\" id=\"policy.banner.id_15_hewtoc\" data-hook=\"consent-banner-section-title\" data-pc-i=\"s3-0-45\">Enable Analytics Cookies</h3><p class=\"sKz7eY\" id=\"policy.banner.id_16_xvigmzoifb\" data-hook=\"consent-banner-section-description\" data-pc-i=\"s3-0-46\">These cookies help us to understand how visitors interact with our website, discover errors and provide a better overall analytics.</p><span data-hook=\"consent-banner-section-toggle\" class=\"dz8xDz _a6Ccw\" data-pc-i=\"s3-0-47\"><input class=\"BfPLBO\" id=\"consent-banner-toggleEnabled-input-id_7\" data-hook=\"consent-banner-section-toggle-input\" aria-labelledby=\"policy.banner.id_15_hewtoc\" aria-describedby=\"policy.banner.id_16_xvigmzoifb\" type=\"checkbox\" data-pc-i=\"s3-0-48\"><label class=\"kCHabv\" for=\"consent-banner-toggleEnabled-input-id_7\" data-pc-i=\"s3-0-49\"><span class=\"NDtop7\" data-pc-i=\"s3-0-50\"></span><span class=\"MezgNL\" data-pc-i=\"s3-0-51\"><svg class=\"tXvr8R n97qfL\" viewBox=\"0 0 11 2\" fill=\"currentColor\" width=\"10\" height=\"2\" data-pc-i=\"s3-0-52\">\n    <path d=\"M0 0H10V2H0z\" data-pc-i=\"s3-0-53\"></path>\n      </svg><svg class=\"tXvr8R Kdinlh\" viewBox=\"0 0 11 8\" fill=\"currentColor\" width=\"10\" height=\"8\" data-pc-i=\"s3-0-54\">\n        <path d=\"M3.8 5L1.2 2.5 0 3.7 3.8 7.5 10 1.2 8.8 0z\" data-pc-i=\"s3-0-55\"></path>\n      </svg></span></label></span></section></section><div class=\"lCXq42\" data-pc-i=\"s3-0-56\"><button data-hook=\"consent-banner-settings-save-button\" class=\"YaqqQl Pg7AcP dukD6Z \" data-pc-i=\"s3-0-57\">Save</button></div></section></div>","parentId":"142","beforeId":null,"position":"fixed"}],"timing":{"appearMs":8.8,"settleMs":46.5,"exitMs":12.5},"animations":[],"closeAnimations":[],"startSamples":[{"opacity":"1","transform":"none","visibility":"visible"}],"endSamples":[{"opacity":"1","transform":"none","visibility":"visible"}]}];
  var byTrigger = {};
  STATES.forEach(function (s) {
    (byTrigger[s.trigger.id] = byTrigger[s.trigger.id] || []).push(s);
  });
  var open = {};
  var order = [];

  function q(id) {
    return document.querySelector('[data-pc-i="' + id + '"]');
  }
  function docRect(el) {
    var r = el.getBoundingClientRect();
    return [r.left + window.scrollX, r.top + window.scrollY, r.width, r.height];
  }
  function motion(s) {
    var dur = 0;
    var easing = 'ease';
    (s.animations || []).forEach(function (a) {
      if (a.duration + a.delay > dur) {
        dur = a.duration + a.delay;
        easing = a.easing || easing;
      }
    });
    return { dur: dur || s.timing.settleMs || 0, easing: easing };
  }
  function findTrigger(target) {
    for (var e = target; e && e.nodeType === 1; e = e.parentElement) {
      var id = e.getAttribute('data-pc-i');
      if (id && byTrigger[id]) return { el: e, id: id };
    }
    return null;
  }
  function insidePopup(target) {
    for (var i = order.length - 1; i >= 0; i--) {
      var o = open[order[i]];
      for (var k = 0; k < o.els.length; k++) if (o.els[k] && o.els[k].contains(target)) return o;
      for (var j = 0; j < o.state.roots.length; j++) {
        var rr = o.state.roots[j];
        if (rr.existing && q(rr.id) && q(rr.id).contains(target)) return o;
      }
    }
    return null;
  }

  function setAttr(id, name, value) {
    var e = q(id);
    if (!e) return;
    if (value === null || value === undefined) e.removeAttribute(name);
    else e.setAttribute(name, value);
  }

  function openState(s, triggerEl) {
    if (open[s.id]) return;
    var els = [];
    // elements that already existed (a hidden dialog, a trigger's aria-expanded) are changed in place, so their own CSS transitions run
    (s.changes || []).forEach(function (c) {
      setAttr(c.id, c.name, c.new);
    });
    s.roots.forEach(function (r, idx) {
      if (r.existing) {
        var ex = q(r.id);
        if (ex) els.push(null);
        return;
      }
      var t = document.createElement('template');
      t.innerHTML = r.html;
      var el = t.content.firstElementChild;
      var parent = (r.parentId && q(r.parentId)) || document.body;
      var before = r.beforeId ? q(r.beforeId) : null;
      if (before && before.parentNode !== parent) before = null;
      parent.insertBefore(el, before);
      els.push(el);
      if (r.position === 'absolute' && s.trigger.docRect && !el.style.translate) {
        var now = docRect(triggerEl);
        var dx = now[0] - s.trigger.docRect[0];
        var dy = now[1] - s.trigger.docRect[1];
        if (Math.abs(dx) > 0.5 || Math.abs(dy) > 0.5) el.style.translate = dx + 'px ' + dy + 'px';
      }
      var from = s.startSamples && s.startSamples[idx];
      var to = s.endSamples && s.endSamples[idx];
      var m = motion(s);
      if (from && to && m.dur > 0 && (from.opacity !== to.opacity || from.transform !== to.transform) && el.animate) {
        el.animate([{ opacity: from.opacity, transform: from.transform }, { opacity: to.opacity, transform: to.transform }], { duration: m.dur, easing: m.easing });
      }
    });
    open[s.id] = { state: s, els: els, trigger: triggerEl };
    if (s.kind !== 'toggle') order.push(s.id); // Escape and outside clicks close popups, not switched-on controls
  }

  function closeState(id) {
    var o = open[id];
    if (!o) return;
    order.slice().forEach(function (other) {
      if (open[other] && open[other].state.parent === id) closeState(other);
    });
    delete open[id];
    if (order.indexOf(id) >= 0) order.splice(order.indexOf(id), 1);
    var s = o.state;
    (s.changes || []).slice().reverse().forEach(function (c) {
      setAttr(c.id, c.name, c.old);
    });
    var exit = 0;
    (s.closeAnimations || []).forEach(function (a) {
      exit = Math.max(exit, a.duration + a.delay);
    });
    exit = exit || s.timing.exitMs || 0;
    o.els.forEach(function (el, idx) {
      if (!el) return;
      var from = s.endSamples && s.endSamples[idx];
      var to = s.startSamples && s.startSamples[idx];
      var done = function () {
        if (el.parentNode) el.parentNode.removeChild(el);
      };
      if (exit > 0 && from && to && el.animate) {
        var a = el.animate([{ opacity: from.opacity, transform: from.transform }, { opacity: to.opacity, transform: to.transform }], { duration: exit, easing: 'ease-in' });
        a.onfinish = done;
        a.oncancel = done;
      } else done();
    });
  }

  function closeTop() {
    if (!order.length) return false;
    closeState(order[order.length - 1]);
    return true;
  }

  document.addEventListener(
    'click',
    function (e) {
      var trig = findTrigger(e.target);
      if (trig) {
        var states = byTrigger[trig.id].filter(function (s) {
          return s.trigger.action === 'click' && (!s.parent || open[s.parent]);
        });
        if (states.length) {
          var s = states[0];
          if (open[s.id]) closeState(s.id);
          else openState(s, trig.el);
          var a = e.target.closest ? e.target.closest('a') : null;
          if (a && s.kind !== 'toggle') e.preventDefault();
          return;
        }
      }
      var popup = insidePopup(e.target);
      if (popup) {
        if (e.target.closest && e.target.closest('[role=menuitem],[role=option],[role=menuitemradio],[role=menuitemcheckbox]')) {
          var id = popup.state.id;
          setTimeout(function () {
            closeState(id);
          }, 0);
        }
        return;
      }
      if (order.length) {
        var topId = order[order.length - 1];
        if (!(open[topId] && open[topId].trigger.contains(e.target))) closeState(topId);
      }
    },
    true
  );
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && closeTop()) e.stopPropagation();
  }, true);
  document.addEventListener('mouseover', function (e) {
    var trig = findTrigger(e.target);
    if (!trig) return;
    var s = byTrigger[trig.id].filter(function (x) {
      return x.trigger.action === 'hover' && !open[x.id] && (!x.parent || open[x.parent]);
    })[0];
    if (s) openState(s, trig.el);
  });
  document.addEventListener('mouseout', function (e) {
    var trig = findTrigger(e.target);
    if (!trig) return;
    if (e.relatedTarget && trig.el.contains(e.relatedTarget)) return;
    byTrigger[trig.id].forEach(function (s) {
      if (s.trigger.action === 'hover' && open[s.id] && !(e.relatedTarget && open[s.id].els.some(function (x) { return x && x.contains(e.relatedTarget); }))) closeState(s.id);
    });
  });

  window.__PC_REPLICA = { states: STATES, openIds: function () { return order.slice(); } };
})();
