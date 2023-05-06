# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Altanmya-Nasr Packaging',
    'version': '1.0',
    'sequence': -200,
    'category': 'Inventory/Purchase',
    'depends': ['mrp', 'sale', 'mail', 'hr', 'account', 'contacts', 'stock', 'calendar'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/res_partner_view.xml',
        'views/mrp_production_view.xml',
        'views/mrp_bom_view.xml',
        'views/stock_picking_view.xml',
        'views/product_template_view.xml',
        'views/sale_order_line_view.xml',
        'views/shift_production_view.xml',
        'report/report_info.xml',
        'report/mic_pallet.xml',
        'report/mrp_production_report_template.xml',
        'report/standard_half_page_pallet_sticker.xml',
        'report/standard_small_page_pallet_sticker.xml',
        'report/Order_Confirmation.xml',
        'report/nasrpack_layout.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
