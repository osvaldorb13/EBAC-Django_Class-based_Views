class ProductModel:
    class ProducStateOptions:
        DRAFT = "BR"
    
    state = ProducStateOptions.DRAFT
    
    def is_published(self, state=ProducStateOptions.DRAFT):
        pass
