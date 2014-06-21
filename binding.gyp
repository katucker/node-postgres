{
  'conditions': [
    ['OS=="win"', {
      'variables': {
        'pgconfig': '<!@(cmd /C where /Q pg_config)'
      }
    }, { # 'OS!="win"'
      'variables' : {
        # Find the full path to the pg_config command, since it may not be on the PATH.
        'pgconfig': '<!(find /usr -executable -name pg_config -print -quit)'
      }
    }]
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