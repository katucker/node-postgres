{
  'targets': [
    {
      'target_name': 'binding',
      'sources': ['src/binding.cc'],
      'include_dirs': [
        '<!(node -e "require(\'nan\')")'
      ],
      'conditions' : [
        ['OS=="win"', {
          'conditions' : [
            ['"<!@(cmd /C where /Q pg_config || echo n)"!="n"',
              {
		      	'include_dirs': [
        			'<!@(pg_config --includedir)',
      			],
                'libraries' : ['libpq.lib'],
                'msvs_settings': {
                  'VCLinkerTool' : {
                    'AdditionalLibraryDirectories' : [
                      '<!@(pg_config --libdir)\\'
                    ]
                  },
                }
              }
            ]
          ]
        }, { # OS!="win"
          'conditions' : [
            ['"<!@(find /usr /bin -executable -name pg_config -quit || echo n)"!="n"',
              {
		      	'include_dirs': [
        			'<!@(`find /usr /bin -executable -name pg_config -print -quit` --includedir)',
      			],
                'libraries' : ['-lpq -L<!@(`find /usr /bin -executable -name pg_config -print -quit` --libdir)']
              }
            ]
          ]
        }]
      ]
    }
  ]
}
