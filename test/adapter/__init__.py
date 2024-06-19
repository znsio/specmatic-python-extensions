from specmatic.coverage.coverage_route import CoverageRoute

VALID_COVERAGE_LIST = [
    CoverageRoute("/findAvailableProducts", ["GET"]),
    CoverageRoute("/products", ["POST"]),
    CoverageRoute("/orders", ["POST"]),
    CoverageRoute("/orders/{id}", ["GET", "PUT", "DELETE"]),
    CoverageRoute("/products/{product_id}/orders/{order_id}", ["GET"]),
]
