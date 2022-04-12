#!/bin/bash
while IFS= read line
do
  if [[ $line =~ "openapi_types =" ]]; then
    printf "$line\n"
    printf "        'event_date': 'datetime',\n"
  elif [[ $line =~ "attribute_map =" ]]; then
    printf "$line\n"
    printf "        'event_date': 'eventDate',\n"
  elif [[ $line =~ "self.discriminator = None" ]]; then
    printf "        self._event_date = None\n"
    printf "$line\n"
    printf "        if event_date is not None:\n"
    printf "            self.event_date = event_date\n"
  elif [[ $line =~ "def to_dict" ]]; then
    printf "    @property\n"
    printf "    def event_date(self):\n"
    printf "        return self._event_date\n"
    printf "\n"
    printf "    @event_date.setter\n"
    printf "    def event_date(self, event_date):\n"
    printf "        self._event_date = event_date\n"
    printf "\n"
    printf "$line\n"
  elif [[ $line =~ "local_vars_configuration=None" ]]; then
    printf "$line\n" | sed 's/local_vars_configuration=None/local_vars_configuration=None, event_date=None/'
  else
    printf "$line\n"
  fi
done
