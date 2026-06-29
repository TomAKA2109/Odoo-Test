/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

class DepartmentBadgeWidget extends Component {
    static template = "hr_simple.DepartmentBadgeWidget";
    static props = { ...standardFieldProps };

    get displayName() {
        const value = this.props.record.data[this.props.name];
        return value ? value[1] : "";
    }

    get color() {
        let hash = 0;
        for (let i = 0; i < this.displayName.length; i++) {
            hash = this.displayName.charCodeAt(i) + ((hash << 5) - hash);
        }
        const h = Math.abs(hash) % 360;
        return `hsl(${h}, 60%, 45%)`;
    }
}

registry.category("fields").add("department_badge", {
    component: DepartmentBadgeWidget,
    supportedTypes: ["many2one"],
});
