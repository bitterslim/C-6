from core.Controllers.makes import MakesController
from core.router import Router

router = Router()

router.get('/', MakesController, 'makes')
router.get('/add', MakesController, 'add_make')
router.post('/', MakesController, 'add')

