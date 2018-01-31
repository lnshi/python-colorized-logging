logging_config = {
  'version': 1,
  'incremental': False,
  'disable_existing_loggers': False,

  'root': {
    'level': 'DEBUG',
    'handlers': ['console']
  },

  'filters': {
    'example': {
      '()': 'utils.logging.filters.ExampleFilter'
    }
  },

  'formatters': {
    'plain': {
      'format': '%(asctime)s %(levelname)-8s %(name)s %(message)s'
    },
    'colorized': {
      '()': 'utils.logging.formatters.ColorizedFormatter'
    }
  },

  'handlers': {
    'console': {
      'level': 'DEBUG',
      'class': 'logging.StreamHandler',
      'filters': ['example'],
      'formatter': 'colorized'
    }
  },

  'loggers': {

  }
}
