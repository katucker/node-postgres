{
  'conditions': [
    ['OS=="win"', {
      'variables': {
        'pgconfig': '<!@(cmd /C where /Q pg_config)'
      }
     }
    ],
    [ 
     'OS=="linux"', {
      'variables' : {
        # Find the full path to the pg_config command, since it may not be on the PATH.
        'pgconfig': '<!(find /usr/bin /usr/local/bin /usr/pg* /opt -executable -name pg_config -print -quit)'
      }
     }, { # Default to assumption that pg_config is on the PATH.
      'variables': {
        'pgconfig': 'pg_config'
      }
     }
    ]
  ],
  'targets': [
    {
      'target_name': 'binding',
      'sources': ['src/binding.cc'],
      'include_dirs': [
        '<!(node -e "require(\'nan\')")',
        '<!@(<(pgconfig) --includedir)',
      ],
      'conditions' : [
        ['OS=="win"', {
          'libraries' : ['libpq.lib'],
          'msvs_settings': {
            'VCLinkerTool' : {
              'AdditionalLibraryDirectories' : [
                '<!@(<(pgconfig) --libdir)\\'
              ]
            },
          }
        }, { # OS!="win"
          'libraries' : ['-L<!@(<(pgconfig) --libdir) -lpq']
        }]
      ]
    }
  ]
}
