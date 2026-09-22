<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0635.txt",
      "sha256": "fc28d9e3c4f0e899c654c8918f4111fe0d63e9f9cb08afd05343b88324fa64b8",
      "bytes": 14191
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0fe3013dd5b12072005f0b55d8727c48f5d4017bf8604c1e955ed42e17fec329",
      "bytes": 1422
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "7e5808f7b11b616f1792ff0096317d4ac49802e47fa719fc9dc90293060f982f",
      "bytes": 195314
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "c634918cabf3494de0bc5462a7ea43a2287339fc442cc90f85c5853f0d6c5eb7",
      "bytes": 517
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "7d549670b039e37e1626809d9c9cc34ae6047c5240d5c1c380611096a76e6643",
      "bytes": 553
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "27e2b56fb8524e2448462c0d5edc198ff3a331a986a14ae361a9bceb906db545",
      "bytes": 1702
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "541073953106750b6abb32638b49fe86703bc02e1ae6faa261d2aca8fa5dffad",
      "bytes": 699
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "16df5acdbc3643214d2c49a1d787152817b5c518c4f95d274e503b100541321e",
      "bytes": 1252
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "6740ff53d01084f73fbfa679cca9a389d32f54868fc0772e87910b5213ae8850",
      "bytes": 528
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "0e490e0d52149b15493ef49653daf299129f8eef5baced807e578915f225a97b",
      "bytes": 871
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ecf6b273109b7892f88c463ff1ff72ed507c43730a0a720a5c6a7c28b9af5717",
      "bytes": 201674
    }
  ],
  "estimated_tokens": 11401
}
-->

# Durable State Update — Chapter 635

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 635. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 635. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 635,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 635,
    "continuity_sources": [635],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "Ailao Mountain has been a forbidden zone for more than a century, guarded by three hundred rotating elite Nanman warriors and subject to annual small-scale exterminations led by the four great chieftains.",
    "More than a hundred elite warriors stationed at Ailao Mountain have been massacred by varied physical attacks and deadly poison, while most of their accompanying beasts are unaccounted for.",
    "Jin Taekyung and the Beast Miao King are investigating the Ailao Mountain crisis under the active time-limited quest.",
    "A giant Black Tiger has appeared at the massacre site, and the system identifies it as Ailao Mountain's Wraith."
  ],
  "continuity_sources": [
    634,
    633
  ],
  "open_questions": [
    "Did Dark Heaven cause the Ailao Mountain massacre, did the mountain's venomous beasts act independently, or are the beasts being controlled by Dark Heaven?",
    "Why are nearly all of the warriors' accompanying beasts missing from the massacre site?",
    "What is the relationship between the giant Black Tiger and Ailao Mountain's Wraith?",
    "Can Jin Taekyung and the Beast Miao King identify the attacker before the investigation timer expires?"
  ],
  "safe_through": 634,
  "temporary_decisions": [
    "Use Black Tiger for 흑호.",
    "Use Ailao Mountain's Wraith for 애뇌산의 망령.",
    "Use Transcendent for 초일류."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 십왕     | **Ten Kings**       |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 시스템              | **System**                     |
| 체력               | **Stamina**                    |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 산군 | **mountain lord** | Traditional epithet for a tiger; retain an explanatory footnote on first use. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 오독문 | **Five Poisons Sect** | Formerly dominant Nanman faction destroyed by the Fire Gate Clan. |
| 영물 | **spiritual creature** | Known non-human creature contrasted with unheard-of monsters. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 흑호 | **Black Tiger** | A colossal black tiger that appears at the Ailao Mountain massacre site. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 수신룡 | legendary_martial_master_to_dying_spirit_beast | you | wary and trembling | Jeok asks what the Water God Dragon is after witnessing its mental communication. |
| 문경 | 수신룡 | physician_to_dying_spirit_beast | you | guarded and curious | Mungyeong asks whether the Water God Dragon knows him. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 문경 | 남천마후 | legendary_assassin_to_hostile_demon_empress | you | polite and grave | Warns her to stop the killing. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 634
- **Aliases:** None
- **Role:** The Beast Miao King is the ruler of the Nanman Beast Palace and oversees its warriors and beasts.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace and is responsible for the forces stationed at Ailao Mountain.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 634
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 634
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 535
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 629
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; he was the sole survivor of an assassin training cohort that began with three hundred candidates and passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance whom Mungyeong helped break free of his Heart Demon, Mungyeong was asked to look after and instruct Jin Taekyung and has now ended that direct training after teaching him martial principles and giving him a custom fire-qi pill, Cheongpung is accompanying him while learning his martial arts through observation, and Mu Song plus five Water Dragon Stronghold subordinates know he is an exceptionally powerful master but not that he is the Slaughter Saint.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 627
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 633
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger, and a halting but capable speaker of Han Chinese.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and Yayul Mok's father; Yayul Mok is his only surviving son after three older siblings died in the Great Faction War, Baeksang is his father's sworn younger brother, and his white tiger is a long-bonded companion.

## Korean source

```text
＃635화



띠링.



- [애뇌산의 망령(亡靈)]이 나타났습니다!



애뇌산의 망령.

본 적도, 들은 적도 없는 존재와 이름.

그러나 새롭게 전달받은 정보를 미처 이해하기도 전에, 시스템으로부터 애뇌산의 망령이라 칭해지는 거대한 흑호(黑虎)가 천둥 같은 포효를 내질렀다.

- 크와아아앙!

어둠을 찢으며 산 전체를 울리는 포효에, 주위의 공기가 물결처럼 일렁이고 풀이며 나뭇가지가 산산이 부서진다.

그것은 단순한 맹수의 울부짖음이 아니었다.

마음속 깊숙한 곳에 숨어 있던 두려움을 불러일으키고, 나아가 심령(心靈)마저 뒤흔드는 원초적인 무언가였다.

그리고 나는 이 힘의 정체를, 이 세상에서 누구보다 잘 알고 있는 사람이었고.

‘피어(Fear).’

처음 놈의 청백색 눈동자를 마주한 순간부터 본능적으로 깨달았다.

갑작스럽게 나타난 저 거대한 맹수는 짐승이라는 두 글자로 완전히 담을 수 없는 존재라는 것을.

그리고 이러한 느낌이 마냥 낯설게 느껴지지 않는 이유는, 이미 몇 달 전 호북에서 놈과 닮은 어떤 존재를 맞닥트린 경험 덕분이었다.

‘수신룡(水神龍).’

암천에 의하여 이지를 상실한 채 미쳐 날뛰던 동정호의 주인. 수백 년의 세월 끝에 새로운 영역으로 접어든 희대의 영물.

나는 태산처럼 우뚝 선 흑호에게서 수신룡과 같은 기운을 읽었고, 그것은 비단 나 혼자만 느낀 것이 아니었다.

- 끄으으응…….

평범한 기준에는 영물이라 칭하기에 부족함이 없는 백호였지만, 강렬한 피어를 이기기에는 역부족이었다.

하지만 겁먹은 강아지처럼 끙끙거리는 녀석과는 달리, 또 다른 누군가는 한 치의 망설임도 없이 앞으로 나섰다.

“네놈의 소행이더냐!”

콰앙!

분노가 가득 담긴 외침과 함께, 힘껏 지면을 박찬 야수묘왕의 신형이 눈 깜짝할 사이에 십여 장의 거리를 지우며 쏘아진다.

어느새 힘껏 말아쥔 주먹에서 눈부신 광휘(光輝)가 터져 나왔다.

후우웅!

묵직한 파공성. 주먹을 실타래처럼 휘감은 파괴적인 강기가 막아서는 모든 것을 지우며 나아갔다.

그리고 그 끝에…….

솨아아악!

아무것도 없는, 텅 빈 허공이 있었다.

“……!”

“……!”

피했다. 다른 누구도 아닌 십왕(十王)에 속한 초절정 고수의 일권을.

그야말로 찰나지간에 벌어진 일이었고, 어둠 속에서 안개처럼 움직여 야수묘왕의 공격을 피한 흑호는 밤처럼 까맣고 커다란 자신의 앞발을 휘둘렀다.

쉬익!

믿을 수 없을 만큼 빠르고. 강맹하게.

꽈앙! 콰드드득!

굉음과 함께 막대한 충격파가 사방을 휩쓸었다. 순간적으로 가해진 거력을 버티지 못하고 밀려난 야수묘왕이 눈을 부릅떴다.

“이게 무슨……!”

그러나 그에게는 경악할 만한 시간조차 충분히 주어지지 않았다. 먹잇감을 앞에 둔 배고픈 맹수는 망설이지 않는 법이니까.

- 크아아앙!

다시 한번 터져 나온 외침이 애뇌산을 뒤흔들었다.

게이트와 몬스터가 상식이자 일상이 되어 버린 현대라면 모를까. 이 세상의 무림인들은 피어에 익숙하지 않다.

더군다나 예상을 아득히 뛰어넘는 규격 외의 존재를 처음으로 조우하게 되어 당황한 야수묘왕의 경우에는 더더욱 그럴 수밖에 없었다.

“흡!”

아주 미세한 경직. 야수묘왕으로서는 최선의 결과였겠지만, 높은 경지에 이른 이들의 생사결은 바로 그 한순간에 노출된 틈새로 결정되는 법.

상대가 무인이 아닌 맹수라 해도 그 사실은 달라지지 않는다.

쉬이이익!

느려진 세상 속, 흡사 갈고리와도 같은 흑호의 발톱이 바람을 찢은 그때.

내 손아귀를 떠난 한 자루의 창이 눈부신 빛줄기가 되어 공간을 가로질렀다.

쐐애애액! 콰앙!

하늘이 쪼개지는 굉음과 함께 반경 십여 장의 공간이 뒤흔들린다.

기운과 기운. 힘과 힘의 격돌.

그리고 짧은 순간 벌어진 격돌의 승자는 바로 나였다.

콰드드득!

창과 한 몸이 되어 뒤로 튕겨 나간 거대한 흑호의 몸뚱어리가 어둠이 내려앉은 숲 너머로 사라지자, 저 멀리 한곳에 모여 있던 수십 그루의 거목이 꺾이고 흔들렸다.

진즉 잠에서 깨어 숨죽인 채 이곳을 바라보고 있었을 산 새가 일제히 날아오르고, 수많은 잎사귀와 나뭇가지가 소나기처럼 쏟아졌다.

투둑. 파사삭!

놈을 잡으려면 바로 지금이 적기다.

그러나 곧장 흑호를 쫓아가려던 나는 이내 얼마 되지 않아 걸음을 멈출 수밖에 없었다.

‘어째서 기척이…….’

기척이 느껴지지 않는다. 조금도.

그나마 있는 단서라고는 폭탄이라도 터진 것처럼 난장판이 된 잔해와 창날이 부서진 채로 떨어져 있는 창 한 자루가 전부.

그 외에는 어떤 족적이나 혈흔도 찾아볼 수 없었다.

‘내 기감의 범위를 벗어났다고? 그것도 이 정도로 빠르게?’

주위를 노려보고 있던 그때. 백호와 함께 달려온 야수묘왕이 분노와 부끄러움이 뒤섞인 표정으로 입을 열었다.

“놈은?”

“도망친 것 같습니다. 찾을 수가 없어요.”

“……빌어먹을. 못 볼 꼴을 보였군.”

“이해합니다. 빈말이 아니라 진심으로요.”

문경과 적천강도 수신룡이 발산하는 피어에 잠시나마 동요했던 적이 있었다.

야수묘왕은 십왕에 꼽힌 만큼 대단한 고수지만, 인외(人外)의 경지에 다다른 두 사람과 비교하는 것은 무리다.

오히려 역으로 생각하면 야수묘왕은 짐작했던 것 이상으로 빠르게 피어의 영향에서 벗어난 셈이었다.

그것이 남만이라는 지역의 특성상 어릴 적부터 기이한 독물이나 맹수들을 자주 접해서인지는 모르겠지만.

그나저나 지금 당장 중요한 건…….

“놈이 아직 살아 있습니다. 혈흔이 없는 걸 보니 딱히 상처를 입은 것 같지도 않고요.”

낮게 깔린 내 목소리에 야수묘왕이 고개를 끄덕였다.

“그럴 것 같았다. 피하지 못할 것을 알자 마지막 순간에 창날을 물더군. 그것도 분명히 강기가 서려 있던 창날을. 남만에서 일평생을 살았지만 저런 놈은 지금까지 본 적도, 들은 적도 없다.”

“그건 아닐걸요.”

“아니라니. 뭘 말이냐?”

“마지막에 하셨던 말씀이요.”

야수묘왕이 뭐라 대답하기도 전에, 나는 담담하게 말을 이었다.

“본 적이 없더라도, 들은 적은 있으실 겁니다. 분명히.”

당장은 기척이 느껴지지 않지만, 언제 다시 놈이 튀어나올지 모르는 상황.

자연스럽게 나와 등을 맞댄 채 주위를 경계하던 야수묘왕의 몸이 흠칫 굳었다.

“혹시.”

“아마도 지금 생각하고 계신 게 맞을 겁니다. 호북성에서 비슷한 일이 있었거든요.”

“……그 이무기를 말하는 것이냐?”

신음처럼 중얼거린 야수묘왕이 말을 이었다.

“무림맹으로부터 받은 서신에 그런 내용이 있긴 했지. 하지만 내심 허황된 이야기라 여겼다.”

“아니, 남만야수궁주 맞습니까? 당장 하나뿐인 아들놈이 백호를 타고 돌아다니는 마당에 그걸 왜 못 믿어요?”

“백호를 타지, 이무기를 타고 있지는 않으니까.”

“……아.”

그것도 그러네.

하긴 이무기는 신화 속에서나 등장하는 존재다. 정보의 출처가 무림맹이라고 해도 쉽게 믿어지지 않는 건 당연하지.

짧고 굵은 대답에 할 말이 없어진 나를 향해, 야수묘왕이 불쑥 입을 열었다.

“그렇다면 방금 나타났던 놈도 남천마후, 그 요녀(妖女)의 손이 닿은 것이냐?”

“확신은 못 합니다. 하지만 그럴 가능성이 높겠죠.”

아니라고 단언하기에는 석연치 않은 점이 한둘이 아니다.

옛 오독문의 본거지였다고는 하나 장장 백여 년 동안이나 잠잠했던 애뇌산에서 갑작스럽게 이런 참사가 벌어진 것도, 갑작스럽게 등장한 흑호의 강력함도 과거의 수신룡과 겹쳐 보이는 듯했다.

‘애뇌산의 망령이라니.’

도대체 놈의 진정한 정체가 뭘까.

이 자리에 싸늘한 주검이 되어 널브러진 이들 외에도 남아 있어야 할 이백 명의 전사와 그들이 부리는 맹수들은 어디에 있는 것일까.

내가 무거운 눈빛으로 주위를 훑어보던 그 순간.

- 크르륵.

피어의 영향에서 간신히 빠져나왔던 백호가 갑자기 자세를 낮추고 꼬리를 바짝 치켜세웠다.

그 사실이 의미하는 바를 깨달은 나와 야수묘왕이 반사적으로 고개를 돌렸을 때, 저 멀리에서는 어둠이 일렁이고 있었다.

‘저건……!’

나도, 야수묘왕도 다른 이야기를 나누느라 잠시 간과하고 있었다.

동물의 후각은 인간보다 수십. 수백 배는 뛰어나며, 주로 밤에 사냥을 나서는 호랑이는 그만큼 후각이 뛰어나다는 것을.

그 말은 즉.

‘이 녀석의 후각이, 내가 느낄 수 있는 기감의 범위보다 넓다.’

한 줄기 깨달음과 동시에, 나와 야수묘왕은 동시에 지면을 박찼다.



* * *



놈을 쫓는 과정에서 똑똑히 알게 됐다.

왜 사람들이 호랑이를 산군(山君)이라 부르는지.

‘아. 저 씨벌놈 보게.’

나는 내심 욕을 삼키며 저 멀리 달려나가는 검은 동체(動體)를 노려보았다.

굽이굽이 진 산줄기를 아무리 달려도, 구름과 안개에 덮인 봉우리를 타고 넘어도 놈을 따라잡을 수가 없다.

놈은 강력한 힘과 지치지 않는 체력. 그리고 신출귀몰한 움직임으로 시종일관 나와 야수묘왕을 앞질렀고, 어디 가서 흰 털 좀 뱉는다는 영물인 백호조차 놈을 따라잡을 수 없었다.

아니, 오히려 점점 불안해하고 있었다.

‘그럴 만도 하지. 상대는 평범한 호랑이가 아니니까.’

산군은 산의 왕이라는 뜻 외에도 산신령을 칭하는 단어이기도 한데, 저놈은 애뇌산의 신령이 아니라 망령이다. 아니, 어쩌면 그보다 더 불길한 악령(惡靈)에 가까울 수도 있다.

그리고 쉴 새 없이 흑호를 쫓아 이동하는 도중에 목격한 광경으로 인하여, 그런 생각은 더더욱 굳혀졌다.

“이런 찢어 죽일……!”

용암처럼 끓어오르는 듯한 음성. 야수묘왕의 분노어린 시선이 향한 곳에는 사지를 축 늘어트린 채 절명한 시신들이 있었다.

깊은 골짜기와 절벽 끄트머리. 한때는 맑았을 테지만 이제는 독으로 인해 검게 물든 계곡…….

남만 전사들의 시신은 우리가 향하는 길을 따라 이정표처럼 쓰러져 있었고, 바람에 섞여든 혈향과 악취는 지독했다.

“감히, 감히 이런 짓을 벌이다니!”

주위를 스쳐 지나가는 참혹한 광경을 확인한 야수묘왕의 전신에서 광포한 기파가 흘러넘쳤다.

지금 이 순간 그는 어느 때보다 분노하고 있었고, 그만큼 움직임은 거칠어졌다.

“노옴!”

타닥, 쐐애애액!

일순간. 가공할 속도로 뻗어 나간 신형이 흑호를 향해 거침없이 쏘아진다.

그러나 상대는 애뇌산의 망령이라고까지 불리는 존재. 정면 대결이라면 모를까. 타고난 신체적 조건과 속도로는 당해 낼 수 없다.

파팟!

예상했던 대로다.

평범한 영물의 한계를 벗어난 흑호는 붙잡히기는커녕 더욱 빠르게 거리를 벌렸고, 이내 어느 깊고 검은 골짜기 사이로 모습을 감췄다.

마치, 올 테면 와 보라는 듯한 눈빛과 함께.

‘뭐지?’

나는 그제야 발걸음을 늦추며 주위를 훑었다.

나이를 알 수 없는 거목과 넝쿨들로 온 사방이 빽빽하고, 안개가 뒤섞인 후텁지근한 공기 사이로 독 특유의 악취가 전해져 온다.

이곳이 정확히 어디인지는 모르겠지만, 정신없이 놈을 쫓아 달리다 보니 애뇌산의 중심부에 도달했다는 것만큼은 짐작할 수 있었다.

‘이건.’

느낌이 좋지 않다. 정말로.

하지만 서서히 걸음을 늦추는 나와는 달리, 곧장 골짜기 내부로 쇄도하는 야수묘왕의 뒷모습에서는 일말의 망설임도 찾아볼 수 없었다.

“야율 대협. 잠시……!”

콰드득!

말릴 새도 없었고, 설령 말렸더라도 야수묘왕은 내 말을 듣지 않았을 것이다.

약간의 분노는 느슨해진 정신을 일깨우지만, 한계를 벗어난 분노는 정신을 잠재우는 법이니까.

“염병.”

작게 욕설을 중얼거린 나는 어느새 얌전해진 백호를 바라보았다.

벌써부터 불길한 낌새를 느낀 듯, 초조한 기색으로 야수묘왕이 사라진 골짜기 입구를 서성이던 녀석은 나와 시선이 마주치자 마치 사람처럼 고개를 내저어 보였다.

“방금 그거. 위험하다는 뜻이냐?”

- 크릉.

“이 자식 이거 똑똑한 거 보소. 처음으로 생각이 일치했네. 그런데 이번에는 어쩔 수가 없다.”

- 크르륵…….

“너까지 따라올 필요는 없으니 이쯤에서 돌아가. 그리고 네 주인이나 다른 사람들을 만나면 전해. 우리가 여기에 있다고.”

영물 축에 들 만큼 똑똑한 녀석이니, 내 말을 충분히 이해했으리라 믿는다.

나는 야율목이 했던 것처럼 백호의 미간을 부드럽게 쓸어 준 뒤, 골짜기를 향해 걸음을 내디뎠다.

한 점의 두려움도 없이. 보무도 당당하게.

“…….”

살아 돌아올 수는 있겠지?
```

## Final English reading copy

```markdown
# Chapter 635

*Ding.*

> **System**
>
> - **Ailao Mountain’s Wraith** has appeared!

Ailao Mountain’s Wraith.

A being and a name I had never seen or heard of before.

But before I could even process the new information, the colossal Black Tiger identified by the System as Ailao Mountain’s Wraith let out a thunderous roar.

*Gwaaaaaaaaaang!*

Its roar tore through the darkness and reverberated across the entire mountain. The air around us rippled like waves, while grass and branches shattered into pieces.

This was not the howl of an ordinary beast.

It was something primal—something that drew out the fear hidden deep within one’s heart and went on to shake the very soul.

And I was the person in this world who knew the true nature of that power better than anyone.

*Fear.*

I had realized it instinctively from the moment I met those blue-white eyes.

That the enormous beast that had appeared so suddenly was more than the word *beast* could ever encompass.

And the reason this sensation did not feel entirely unfamiliar was that I had encountered something resembling this creature a few months ago in Hubei.

*The Water God Dragon.*

The master of Dongting Lake, who had been driven insane and rampaged after losing its reason to Dark Heaven. A rare spiritual creature that had entered a new realm after several hundred years.

I sensed qi like the Water God Dragon’s emanating from the Black Tiger towering like Taishan, and I was not the only one who felt it.

*Whine…*

By ordinary standards, White Tiger was more than worthy of being called a spiritual creature, but it was no match for that intense Fear.

Unlike the creature whimpering like a frightened puppy, however, someone else stepped forward without the slightest hesitation.

“Was this your doing?”

*Boom!*

With a furious shout, the Beast Miao King kicked off the ground with all his strength. His body shot forward, covering more than ten zhang in the blink of an eye.

Radiant light burst from the fist he had clenched tightly.

*Whoooosh!*

A heavy sound split the air. Destructive Force coiled around his fist like thread, erasing everything in its path as it advanced.

And at its end…

*Slash!*

There was nothing.

Only empty space.

“……!”

“……!”

It had dodged the Beast Miao King’s punch—a blow from a Supreme Peak master belonging to the Ten Kings.

It happened in the blink of an eye. Having moved through the darkness like mist to evade the Beast Miao King’s attack, the Black Tiger swung its enormous front paw, black as night.

*Swish!*

Unbelievably fast.

And terrifyingly powerful.

*Boom! Crack-crack-crack!*

A tremendous shock wave swept in every direction with a deafening roar. The Beast Miao King was pushed back by the immense force delivered in an instant, his eyes widening.

“What the…?”

But he was not even given enough time to be shocked. A hungry predator standing before its prey did not hesitate.

*Gwaaaaaaaaaang!*

Another roar shook Ailao Mountain.

The people of this world were not accustomed to Fear. That might have been different in the modern world, where Gates and monsters had become common sense and everyday life, but not here.

And the Beast Miao King had been caught even more off guard because this was his first encounter with an existence so far beyond anything he had expected.

“Kh!”

It was only the slightest moment of paralysis. For the Beast Miao King, it might have been the best possible outcome, but life-and-death duels between people of great skill were decided by the opening exposed in a single instant.

That fact did not change merely because his opponent was a beast rather than a martial artist.

*Whoosh!*

In a world that seemed to have slowed, the Black Tiger’s claws—resembling hooks—were just about to tear through the air.

At that moment, a spear that had left my hand became a dazzling streak of light and tore across the space between us.

*Shreeeek! Boom!*

A deafening roar split the heavens, and the space within a radius of more than ten zhang shook violently.

Qi against qi.

Strength against strength.

And the victor of that brief clash was me.

*Crack!*

The Black Tiger’s enormous body, sent flying backward as though it had become one with the spear, vanished beyond the forest shrouded in darkness. Far away, dozens of giant trees clustered together snapped and swayed.

The mountain birds that had long since awakened and must have been watching us in silence took flight all at once, while countless leaves and branches poured down like a rain shower.

*Tap. Rustle!*

Now was the perfect time to catch it.

But I had barely begun chasing after the Black Tiger when I was forced to stop.

*Why can’t I sense it…?*

I could not feel its presence.

Not even a trace.

The only clues left behind were the wreckage scattered around as though a bomb had exploded and a spear lying on the ground with its blade shattered.

I could not find any footprints or bloodstains.

*Did it escape the range of my Qi Sense? And that quickly?*

As I glared into the surroundings, the Beast Miao King arrived alongside White Tiger and spoke with an expression mingling anger and shame.

“Where is it?”

“It seems to have run away. I can’t find it.”

“……Damn it. I made a fool of myself.”

“I understand. I really do. I’m not just saying that.”

Mungyeong and Jeok Cheongang had also been shaken, if only briefly, by the Fear emanating from the Water God Dragon.

The Beast Miao King was an incredible master worthy of being counted among the Ten Kings, but it was unreasonable to compare him with those two, who had reached a realm beyond humanity.

If anything, that meant he had broken free of Fear’s influence even more quickly than I had expected.

Perhaps it was because, as a native of Nanman, he had often encountered strange venomous beasts and ferocious animals from an early age.

In any case, what mattered most right now was…

“It’s still alive. There’s no blood, so it doesn’t seem to have suffered any significant injury.”

At my low voice, the Beast Miao King nodded.

“I thought so. When it realized it could not dodge, it bit down on the spearhead at the last moment. And that spearhead was clearly wreathed in Force. I’ve lived my entire life in Nanman, but I’ve never seen or heard of anything like that creature.”

“I don’t think that’s true.”

“What do you mean?”

“What you said at the end.”

Before the Beast Miao King could answer, I continued calmly.

“Even if you’ve never seen it, you must have heard of it. I’m sure of it.”

For now, we could not sense the creature’s presence, but there was no telling when it might leap out again.

The Beast Miao King, who had naturally placed his back against mine while keeping watch over the surroundings, stiffened.

“Could it be…?”

“You’re probably thinking of the right thing. Something similar happened in Hubei Province.”

“……Are you talking about that imugi?”

The Beast Miao King muttered the words like a groan, then continued.

“There was something about that in the letter I received from the Murim Alliance. But I privately thought it was an absurd story.”

“Are you really the Lord of the Nanman Beast Palace? Your only son is riding around on a White Tiger, and you couldn’t believe that?”

“He rides a White Tiger, not an imugi.”

“……Ah.”

Fair enough.

An imugi was something that appeared only in mythology. Even if the information had come from the Murim Alliance, it was only natural that he would have trouble believing it.

His short and decisive answer left me with nothing to say. Then the Beast Miao King suddenly opened his mouth.

“If that is the case, was that creature that just appeared also the work of the Southern Heaven Demon Empress—that witch?”

“I can’t say for certain. But it’s highly likely.”

There were too many suspicious points for me to flatly declare that it was not.

Although Ailao Mountain had once been the headquarters of the Five Poisons Sect, it had remained quiet for more than a hundred years. The sudden massacre that had taken place there, along with the power of the Black Tiger that had appeared out of nowhere, both seemed to overlap with what had happened to the Water God Dragon in the past.

*“Ailao Mountain’s Wraith.”*

What on earth was the creature’s true identity?

Where were the two hundred warriors who should still have been here, aside from the people now sprawled around us as cold corpses? And where were the ferocious beasts they commanded?

I was slowly scanning the area with a heavy gaze when—

*Grrr.*

White Tiger, which had barely recovered from the influence of Fear, suddenly lowered its body and raised its tail straight up.

The Beast Miao King and I realized what that meant and turned our heads reflexively.

Far away, the darkness was rippling.

*That’s…!*

Both the Beast Miao King and I had overlooked something while talking about other matters.

An animal’s sense of smell was dozens, even hundreds of times keener than a human’s. And tigers, which primarily hunted at night, possessed an equally powerful sense of smell.

Which meant…

*This creature’s sense of smell reaches farther than the range of my Qi Sense.*

The instant I realized that, the Beast Miao King and I kicked off the ground at the same time.

* * *

During the chase, I learned exactly why people called tigers mountain lords.[^1]

*Ah. Look at that fucking bastard.*

I stared at the black shape racing far ahead while silently swallowing a curse.

No matter how fast we ran along the winding mountain ridges, no matter how many cloud-shrouded, mist-covered peaks we crossed, we could not catch up.

With its tremendous strength, inexhaustible Stamina, and elusive movements, the creature stayed ahead of the Beast Miao King and me from start to finish. Even White Tiger—a spiritual creature that could boast some pretty impressive white fur—could not catch it.

No. White Tiger was growing increasingly anxious instead.

*It makes sense. Its opponent isn’t an ordinary tiger.*

The word *mountain lord* did not merely mean the king of the mountain. It was also a term for a mountain spirit. But that creature was not the spirit of Ailao Mountain.

It was its wraith.

No—perhaps it was closer to an even more ominous evil spirit.

And the sights I witnessed while endlessly chasing the Black Tiger only reinforced that thought.

“That damned beast…!”

His voice seemed to boil like molten lava. The Beast Miao King’s furious gaze was fixed on corpses whose limbs hung limp.

Deep valleys. The edges of cliffs. Ravines that must once have run clear but had now been stained black by poison…

The corpses of Nanman warriors lay along the path we were taking like signposts, and the stench of blood and decay carried on the wind was unbearable.

“How dare they? How dare they do something like this!”

A savage aura poured from the Beast Miao King’s entire body as he took in the horrific scenes flashing past us.

He was angrier at that moment than I had ever seen him, and his movements became that much rougher.

“You bastard!”

*Tap-tap—shreeeek!*

In an instant, his body shot forward at a terrifying speed and streaked toward the Black Tiger without hesitation.

But the opponent was a being known as Ailao Mountain’s Wraith. A direct confrontation might have been another matter, but the Beast Miao King could not match its natural physique and speed.

*Papat!*

Just as expected.

The Black Tiger had surpassed the limits of an ordinary spiritual creature. Rather than being caught, it widened the distance even further and soon vanished into a deep, dark valley.

It gave us a look as though to say, *Come and get me if you dare.*

*What?*

Only then did I slow down and look around.

Ancient trees and vines filled every direction, while the hot, humid air mixed with mist carried the distinctive stench of poison.

I did not know exactly where we were, but after running mindlessly in pursuit of the creature, I could at least guess that we had reached the heart of Ailao Mountain.

*This is…*

I had a very bad feeling.

A truly bad feeling.

Unlike me, who was gradually slowing down, the Beast Miao King charged straight into the valley. There was not even the slightest hesitation in his retreating figure.

“Great Hero Yayul, wait—!”

*Crack!*

I had no time to stop him. And even if I had, the Beast Miao King would not have listened.

A little anger could rouse a slackened mind. But anger that went beyond its limits could put the mind to sleep.

“Damn it.”

I muttered the curse under my breath and looked at White Tiger, which had suddenly grown quiet.

As though it had sensed the ominous signs already, it paced anxiously around the entrance to the valley where the Beast Miao King had disappeared. When its eyes met mine, it shook its head like a person.

“Was that supposed to mean it’s dangerous?”

*Grrr.*

“This guy’s pretty smart. We agreed for the first time. But there’s nothing we can do this time.”

*Grrr…*

“You don’t have to follow me, so turn back here. And if you meet your master or anyone else, tell them we’re here.”

It was intelligent enough to be counted among spiritual creatures, so I trusted that it understood me.

As Yayul Mok had done, I gently stroked White Tiger between the eyes, then stepped toward the valley.

Without a trace of fear.

With my head held high.

“……”

*I’ll be able to make it back alive, right?*

[^1]: *San-gun*, literally “mountain lord,” is a traditional epithet for a tiger and can also refer to a mountain spirit.
```
