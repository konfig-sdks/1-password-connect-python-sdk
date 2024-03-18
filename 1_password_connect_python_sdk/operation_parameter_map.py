operation_parameter_map = {
    '/activity-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/vaults/{vaultUuid}/items/{itemUuid}/files-GET': {
        'parameters': [
            {
                'name': 'vaultUuid'
            },
            {
                'name': 'itemUuid'
            },
            {
                'name': 'inline_files'
            },
        ]
    },
    '/vaults/{vaultUuid}/items/{itemUuid}/files/{fileUuid}/content-GET': {
        'parameters': [
            {
                'name': 'vaultUuid'
            },
            {
                'name': 'itemUuid'
            },
            {
                'name': 'fileUuid'
            },
        ]
    },
    '/vaults/{vaultUuid}/items/{itemUuid}/files/{fileUuid}-GET': {
        'parameters': [
            {
                'name': 'vaultUuid'
            },
            {
                'name': 'itemUuid'
            },
            {
                'name': 'fileUuid'
            },
            {
                'name': 'inline_files'
            },
        ]
    },
    '/heartbeat-GET': {
        'parameters': [
        ]
    },
    '/health-GET': {
        'parameters': [
        ]
    },
    '/vaults/{vaultUuid}/items-POST': {
        'parameters': [
            {
                'name': 'vaultUuid'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'title'
            },
            {
                'name': 'version'
            },
            {
                'name': 'id'
            },
            {
                'name': 'vault'
            },
            {
                'name': 'category'
            },
            {
                'name': 'urls'
            },
            {
                'name': 'favorite'
            },
            {
                'name': 'state'
            },
            {
                'name': 'createdAt'
            },
            {
                'name': 'updatedAt'
            },
            {
                'name': 'lastEditedBy'
            },
            {
                'name': 'sections'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'files'
            },
        ]
    },
    '/vaults/{vaultUuid}/items/{itemUuid}-DELETE': {
        'parameters': [
            {
                'name': 'vaultUuid'
            },
            {
                'name': 'itemUuid'
            },
        ]
    },
    '/vaults/{vaultUuid}/items-GET': {
        'parameters': [
            {
                'name': 'vaultUuid'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/vaults/{vaultUuid}/items/{itemUuid}-GET': {
        'parameters': [
            {
                'name': 'vaultUuid'
            },
            {
                'name': 'itemUuid'
            },
        ]
    },
    '/vaults/{vaultUuid}/items/{itemUuid}-PUT': {
        'parameters': [
            {
                'name': 'vaultUuid'
            },
            {
                'name': 'itemUuid'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'title'
            },
            {
                'name': 'version'
            },
            {
                'name': 'id'
            },
            {
                'name': 'vault'
            },
            {
                'name': 'category'
            },
            {
                'name': 'urls'
            },
            {
                'name': 'favorite'
            },
            {
                'name': 'state'
            },
            {
                'name': 'createdAt'
            },
            {
                'name': 'updatedAt'
            },
            {
                'name': 'lastEditedBy'
            },
            {
                'name': 'sections'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'files'
            },
        ]
    },
    '/vaults/{vaultUuid}/items/{itemUuid}-PATCH': {
        'parameters': [
            {
                'name': 'vaultUuid'
            },
            {
                'name': 'itemUuid'
            },
        ]
    },
    '/metrics-GET': {
        'parameters': [
        ]
    },
    '/vaults/{vaultUuid}-GET': {
        'parameters': [
            {
                'name': 'vaultUuid'
            },
        ]
    },
    '/vaults-GET': {
        'parameters': [
            {
                'name': 'filter'
            },
        ]
    },
};