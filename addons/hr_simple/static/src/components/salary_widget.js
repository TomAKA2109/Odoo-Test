/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

class SalaryWidget extends Component {
    static template = "hr_simple.SalaryWidget";
    static props = { ...standardFieldProps };

    get salary() {
        return this.props.record.data[this.props.name] || 0;
    }

    get maxSalary() {
        return 50000000; // 50 triệu
    }

    get percentage() {
        return Math.min((this.salary / this.maxSalary) * 100, 100).toFixed(0);
    }

    get color() {
        if (this.percentage < 30) return "#ff4444";
        if (this.percentage < 70) return "#ffaa00";
        return "#00aa44";
    }

    onSalaryChange(ev) {
        this.props.record.update({ [this.props.name]: parseFloat(ev.target.value) || 0 });
    }
}



registry.category("fields").add("salary_widget", {
    component: SalaryWidget,
    supportedTypes: ["float"],
});
