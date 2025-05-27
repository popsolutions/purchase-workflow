# Copyright 2025 PopSolutions
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestPurchaseRequestLines(TransactionCase):
    def setUp(self):
        super().setUp()
        self.request_model = self.env["purchase.request"]
        self.line_model = self.env["purchase.request.line"]
        self.product = self.env.ref("product.product_product_1")
        self.uom = self.env.ref("uom.product_uom_unit")
        self.picking_type = self.env.ref("stock.picking_type_in")

        self.request = self.request_model.create(
            {
                "requested_by": self.env.user.id,
                "picking_type_id": self.picking_type.id,
            }
        )

    def test_sequence_assignment(self):
        # Criação de múltiplas linhas e verificação da sequência
        line1 = self.line_model.create(
            {
                "request_id": self.request.id,
                "product_id": self.product.id,
                "product_uom_id": self.uom.id,
                "product_qty": 1,
            }
        )
        line2 = self.line_model.create(
            {
                "request_id": self.request.id,
                "product_id": self.product.id,
                "product_uom_id": self.uom.id,
                "product_qty": 2,
            }
        )
        line3 = self.line_model.create(
            {
                "request_id": self.request.id,
                "product_id": self.product.id,
                "product_uom_id": self.uom.id,
                "product_qty": 3,
            }
        )

        self.assertEqual(line1.sequence, 1)
        self.assertEqual(line2.sequence, 2)
        self.assertEqual(line3.sequence, 3)

    def test_sequence_after_delete(self):
        # Cria 3 linhas, remove uma, verifica se a sequência é atualizada
        line1 = self.line_model.create(
            {
                "request_id": self.request.id,
                "product_id": self.product.id,
                "product_uom_id": self.uom.id,
                "product_qty": 1,
            }
        )
        line2 = self.line_model.create(
            {
                "request_id": self.request.id,
                "product_id": self.product.id,
                "product_uom_id": self.uom.id,
                "product_qty": 2,
            }
        )
        line3 = self.line_model.create(
            {
                "request_id": self.request.id,
                "product_id": self.product.id,
                "product_uom_id": self.uom.id,
                "product_qty": 3,
            }
        )

        line2.unlink()
        self.request.invalidate_cache()
        self.request.line_ids._compute_sequence()

        self.assertEqual(line1.sequence, 1)
        self.assertEqual(line3.sequence, 2)
