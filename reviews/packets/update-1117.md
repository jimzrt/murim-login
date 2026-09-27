<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1117.txt",
      "sha256": "9647fce3ea0f0e3457f2d4dbeb852c08cb83efd4e970b930343a6ed043e95c90",
      "bytes": 15466
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d9903bb6d1f6d89695be134856ed01159bb7809068541d88848a121abfdc31e3",
      "bytes": 1027
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "66b724f4d846741f2cbbc7e843d83ef54cdbfc708dd1f9b56308f753f4d5a999",
      "bytes": 244911
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "10b70ea99837c80d906e458d11a74478421efcf660f8a94e5612c202166e4bff",
      "bytes": 915
    },
    {
      "path": "characters/Cheongheoja.md",
      "sha256": "8d2417ba0af73148119b8dafd4ec6bf9e9168d11e59ca18ca4c61b134b1badd0",
      "bytes": 557
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "85bc9a5a9407199b349dba3b9bcf170e64dfb000ff63ef7a007128617a9e841b",
      "bytes": 760
    },
    {
      "path": "characters/Hak Su.md",
      "sha256": "e37e1c13cfb6d52828f5d60683a7008be5bff2c6d37e7eb77c54b64ec0b0395e",
      "bytes": 665
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "eed2360e9a384fc08e9b2298aacd8e15d606fdd798c0b6e0b754b49990c19bbd",
      "bytes": 668
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "6a30ea0d70bf482b66155b28050950fe68b7e4dd847cdbda9ac09cc336a20c1e",
      "bytes": 959
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "d6a34d79ef14c6305b220f29edf65d9fe3b6a2f351c2d0c98377fcde7f60e3da",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d55475543ec1fb1c82a8c660ed8fc6b6c7536abad3e5c84ebccc42321005d0fd",
      "bytes": 289267
    }
  ],
  "estimated_tokens": 11156
}
-->

# Durable State Update — Chapter 1117

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 1117. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1117. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
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
  "chapter": 1117,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1117,
    "continuity_sources": [1117],
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
    "The West Gate has fallen, and the South Gate defenders were ordered to retreat to the Inner City.",
    "Cheongheoja plans to lead the East Gate forces to the Inner City but remains at the East Gate with Hak Su and the revealed spies.",
    "Hak Eui is alive; a disguised prisoner's corpse led others to believe he had been killed.",
    "Hak Su is a Dark Heaven spy known as Number Six; five other embedded spies have revealed themselves and taken Temporary Strength Pills.",
    "The Slaughter Saint helped conceal Hak Eui's survival by making a human-skin mask."
  ],
  "continuity_sources": [
    1115,
    1116
  ],
  "open_questions": [
    "What will happen in the East Gate confrontation between Cheongheoja, the Kunlun defenders, and the spies?",
    "Will the East Gate forces reach the Inner City, and what awaits them there?"
  ],
  "safe_through": 1116,
  "temporary_decisions": [
    "Render 육호 as “Number Six” for Hak Su’s Dark Heaven identifier."
  ],
  "version": 1
}
```

## Exact glossary matches

| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 곤륜파    | **Kunlun Sect**                  |
| 암천     | **Dark Heaven**                  |
| 장강수로맹  | **Yangtze River Channel League** |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 곤륜     | **Kunlun**             |
| 귀가      | **your family**                                                 |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 청허자 | **Cheongheoja** | Kunlun Sect Leader. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 학수 | **Hak Su** | Cheongheoja’s Senior Disciple and Hak Woo’s senior brother. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 평화 | **Peace Guild** | Guild name. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 황하 | **Yellow River** | River along which civilization began. |
| 녹림투왕 | **Green Forest Battle King** | Epithet of the Green Forest Alliance Leader, distinguished from the Ten Kings. |
| 시취 | **corpse stench** | The odor Taekyung recognizes from the covered body. |
| 제시 | **Jesse** | The U.S. Secretary of State, introduced by first name. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 황도 | **Imperial Capital** | The capital where the imperial court resides. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 서녕 | **Xining** | Capital of Qinghai. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 혈주 | 마삼보 | superior_to_subordinate | you; you fool | hostile and threatening | The Blood Lord berates Ma Sanbao after the surveillance is exposed. |
| 마삼보 | 혈주 | subordinate_to_superior | My Lord | deferential | Ma Sanbao reports to the Blood Lord and pleads for mercy. |
| 태산 | 청허자 | younger martial artist to senior sect leader | you | clipped and childlike | Asks whether Cheongheoja brought meat. |
| 학수 | 청허자 | Disciple addressing his Master | Master | Respectful and formal | Addresses him as 스승님. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1116
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure and formidable combatant who commands weapons telekinetically and absorbs blood to restore vitality.
- **Personality:** Cunning and controlling, he plans around opponents’ strengths and learns from past mistakes; his confidence in his overwhelming power is genuine rather than bluster, and he remains devoted to the Lord of Heaven despite resenting being treated as disposable and Taekyung’s apparent favor.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and suspects the Lord wants Jin Taekyung above all else; he recognizes Cheongpung and remembers a debt to Sword Saint Mae Jonghak.

### Cheongheoja.md

# Cheongheoja (청허자)

- **Safe through:** Chapter 1116
- **Aliases:** None
- **Role:** Cheongheoja is the Kunlun Sect Leader and Hak Woo’s master.
- **Personality:** Warm, composed, and patient, he faces setbacks with resolve and receives even startling company with good humor.
- **Voice:** Measured and gentle, using formal Daoist courtesies and calm metaphors.
- **Relationships:** Hak Su and Hak Eui are his Disciples; he knows Jin Taekyung by reputation and treats him warmly.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1116
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hak Su.md

# Hak Su (학수)

- **Safe through:** Chapter 1116
- **Aliases:** None
- **Role:** Hak Su is a Dark Heaven spy known as Number Six, formerly Cheongheoja’s Senior Disciple in the Kunlun Sect.
- **Personality:** He is disciplined and mission-bound as a Dark Heaven spy, yet his gratitude and affection for Cheongheoja were genuine.
- **Voice:** He speaks in courteous, formal phrases and tempers earnest reassurance with hearty, lightly humorous remarks.
- **Relationships:** Cheongheoja was his Master, Hak Woo his youngest Junior Brother, and he treated Jin Taekyung warmly as a Fellow Daoist.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 1099
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 1077
- **Aliases:** None
- **Role:** Ma Sanbao is a sorcerer and Supreme Peak martial artist, former disciple of the Eastern Heaven Demon Lord, and servant of the Lord of Heaven, whose power lets him raise the dead within limits and command beasts with ritual bells.
- **Personality:** He is ambitious and confident in his usefulness to the Lord of Heaven, dismissive of his former master’s weakness, and pragmatic about losing subordinates.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao served the Eastern Heaven Demon Lord as his disciple and now serves the Lord of Heaven; he regards Jin Taekyung as an adversary who will make a captured operative betray him.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1106
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1117화



오늘날, 서녕의 그 어디에서도 평화라는 단어는 찾아볼 수 없었다.

동서남북. 심지어는 하늘조차도 마찬가지였다.

온 사방이 비와 핏물에 잠겼고 비명과 굉음은 끊이질 않았다.

그러나 단 한 곳, 동문(東門)으로부터 수백여 장 밖에 우뚝 솟아있는 언덕만큼은 예외였다.

‘정말이지, 끔찍하게도 퍼붓는군.’

생사가 오가는 위기에 처한 이라면 도저히 떠올릴 수 없을 생각.

커다란 구멍이라도 뚫린 것일까, 싶을 정도로 굵은 빗줄기를 쉴 새 없이 쏟아 내는 하늘을 바라보던 흑의인이 문득 동쪽으로 고개를 돌렸다.

쏴아아아.

짙게 내려앉은 어둠 속, 폭풍우와도 같은 거센 바람에 휩쓸려 출렁이는 물결.

며칠간 단 한시도 쉬지 않고 계속된 유례없는 폭우로 인해, 제법 원만한 평지였던 그곳은 어느새 강이라도 불러도 이상하지 않을 정도로 변해 있었다.

물론, 정작 흑의인이 확인하고자 했던 것은 따로 있었지만.

“놈들은?”

곁에 있던 동료가 불쑥 던진 물음에, 흑의인이 대답했다.

“아직.”

“예상보다 늦는군. 지금쯤이면 충분히 도착할 때도 되었는데.”

“시간을 지킬 만큼 근면한 놈들이었다면 왜 도적질이나 하고 살겠나.”

깊게 눌러쓴 흑의 아래, 낮은 웃음소리로 동의를 표한 동료가 말을 이었다.

“하지만 이 정도까지 멍청할 줄은 몰랐어. 비록 근본도 없는 도적놈들이라 해도, 감히 맹(盟)을 자처할 정도라면 어느 정도의 수완이나 눈치쯤은 있을 줄 알았지.”

“글쎄, 어쩌면 나름대로 머리를 굴린 결과일지도.”

“무슨 뜻인가?”

“제아무리 멍청한 종자들이라 해도 화살받이로 쓰이리라는 것쯤은 짐작했을 걸세. 저들 중 대부분은 도적 나부랭이에 불과하지만, 그 수괴(首魁)인 해상왕과 녹림투왕은 제법 머리를 굴릴 줄 알거든.”

“놈들이 피해를 최소화하기 위해 일부러 늑장을 부리고 있다?”

“날씨가 험해진 탓도 있겠지만, 가능성은 충분하지.”

“무려 일만에 달하는 아군이 그 도적놈들을 감시하고 있을 텐데도?”

“누가 알겠나. 제아무리 눈을 부릅뜨고 있어도 장강수로맹의 물귀신들이 작정하고 수작을 부린다면야.”

“허, 만약 그게 사실이라면 멍청한 정도가 아니라 구제불능인데.”

혀를 차는 동료의 모습에 흑의인이 고개를 끄덕였다.

비록 조금 전의 대화에서 직접적으로 언급하지는 않았지만, 한 번 시작되면 뒤가 없이 날뛰는 혈주(血主)의 잔인성은 암천 내에서도 모르는 이가 없을 정도.

만약 장강수로맹과 녹림맹의 연합군이 모든 전투가 끝난 후에야 뒤늦게 도착한다면…….

‘오늘 이후부터 중원의 강산(江山)이 깨끗해지겠지. 도적놈들 따위는 털끝 하나 찾아볼 수 없을 만큼.’

그러나 그런 그들에게도 아직 살아남을 기회는 있었다.

계획에 따라 동문이 열리기 전에 때맞춰 도착하기만 한다면, 최소한의 공이라도 세워 체면을 지킨다면 그 질긴 명줄을 조금이라도 더 연장시킬 수 있을 것이다.

물론, 그 또한 어디까지나 혈주의 기분에 따라 달라지겠지만.

‘살고 싶다면 젖 먹던 힘까지 쥐어 짜내어 노를 젓거라. 그래야 피차 피곤하지 않을 테니.’

저 멀리 한창 전투가 벌어지고 있는 동문을 바라보며, 흑의인은 내심 중얼거렸다.

한낱 도적놈들의 생사 따위가 무슨 상관이겠느냐마는, 암천 내에서 이른바 강시술사(僵尸術士)로 분류되는 그에게는 상당히 중요한 문제였다.

흑의인의 역할은 전장에서 싸우는 병사가 아니라, 전장에 널브러진 시체를 치우는 운반조에 가까웠으니까.

그리고 과도한 업무량을 걱정하는 그의 마음과는 반대로, 동문을 둘러싸고 일진일퇴(一進一退)를 거듭하던 전투의 흐름은 급격하게 뒤바뀌고 있었다.

콰아아앙!

불현듯 울려 퍼지는 굉음.

빗소리는 물론 때때로 내리치던 천둥마저 집어삼킨 그 커다란 소음에, 흑의인과 그 동료는 눈을 크게 떴다.

그와 동시에 그들의 시야에 들어온 것은, 폭발하는 섬광과 함께 무너지는 성벽의 상단이었다.

“저건…….”

흑의인이 신음처럼 뇌까렸다.

비록 찰나였지만, 확신할 수 있었다.

지금 이 순간에도 쉴 새 없이 성벽 위에서 번뜩이고 있는 저 섬광이, 강기(罡氣)라 불리는 파괴적인 기운이라는 것을.

‘왜지? 일부러 맹공을 퍼붓지도 않았는데 청허자가 어째서.’

문득 곤륜파 장문인의 존재가 뇌리를 스쳤지만, 흑의인은 이내 고개를 가로저을 수밖에 없었다.

퍼엉! 구구구궁!

재차 터져 나오는 아득한 섬광.

그것에 담긴 빛은, 도무지 도가(道家)의 무공으로부터 비롯되었다고 말할 수 없을 만큼 희뿌옇고 불길했으니.

“흑귀(黑鬼)도 아닐세. 놈들은 아직 명령대로 제자리를 지키고 있어.”

때마침 들려온 동료의 말은 사실이었다.

두 기의 흑귀는 혈주의 지시에 따라, 일부러 투입하지 않은 상당수의 병력을 거느린 채 성벽 앞 전장에 대기 중이었으니까.

“그렇다는 건.”

흑의인은 문득 말을 멈췄다.

저 강기의 주인이 흑귀도, 청허자도 아니라면 남은 것은 하나뿐이다.

간자(間者).

오랜 세월에 걸쳐 곤륜파에 심어두었던 간자들이 마침내 행동을 개시한 것이다.

그것도 계획되었던 시점보다도 한발 앞서서.

“어떻게 하지?”

동료의 물음에 흑의인은 입술을 깨물었다.

그로서는 참으로 빌어먹을 일이 아닐 수 없었다.

지금쯤 전장에 도착했어야 할 장강수로맹과 녹림맹 연합군은 아직까지도 기약이 없고, 그에 맞춰 동문을 열었어야 할 간자들은 때아닌 교전을 벌이고 있다니.

설상가상으로 그들의 직속상관이라 할 수 있는 마삼보마저 오늘 이 자리에 없었으니, 결국 흑의인이 직접 판단하고 선택할 수밖에 없었다.

그것도 아주 신속하게.

그리고 마치 영원처럼 느껴지는 짧은 시간 속, 수많은 갈등에 사로잡힌 채 동문을 응시하던 흑의인은 불현듯 눈을 부릅떴다.

철컥. 그그그긍!

육중한 마찰음과 함께 천천히 움직이기 시작한 철교(鐵橋).

성문 앞 해자(垓字)와 연결된 그 거대한 다리가, 마치 한 줄기의 빛처럼 내려오고 있었다.

‘철교는 성문과 이어져 있고, 따라서 반드시 내부에서만 작동시킬 수 있다.’

그렇다면 저 광경은 곤륜파에 심어둔 간자들이 내부에서 성문을 열고 있다는 명백한 증거이자 절호의 기회.

더 이상의 고민은, 흑의인에게 있어 무의미했다.

“명하노니, 부름에 답하라!”

흑의인이 외침과 동시에 허리춤에 꽂혀있던 요령(妖鈴)을 꺼내 힘차게 떨쳤다.

우우웅.

음산한 소리와 함께 바람을 타고 뻗어 나가는 파장.

그와 동시에 지금껏 그들이 서 있던 언덕이, 아니 빗줄기와 혼란에 가려져 언덕이라고 착각할 수밖에 없었던 거대한 살덩어리들이 그 강렬한 파장에 응답했다.

드드드득!

지진이라도 일어난 것처럼 땅이 뒤흔들리고. 빗물과 흙에 가려져 있던 끔찍한 시취(屍臭)가 피어오른다.

쿠웅, 쿠우우웅!

전신에 치덕치덕 바른 진흙을 떨치고, 아름드리나무와도 같은 팔다리로 우뚝 선 괴물의 숫자는 도합 일천.

그중 하나의 어깨에 걸터앉은 흑의인이 다시 한번 요령을 흔들며 속삭였다.

“모조리 쓸어버려라.”

그 순간.

- 콰우우우우우!

그 체격에 걸맞는 거대한 포효와 함께, 일천에 달하는 괴물들이 파도처럼 전장을 향해 쏟아졌다.

두두두두두!

황하(黃河)가 범람한다면 이런 광경일까.

누구도 막을 수 없을 정도로 흉포한 기세로 들이닥치는 괴물들을 발견한 성벽 위에서 뒤늦게 비명이 터져 나왔지만, 그들이 상대해야 할 적은 그뿐만이 아니었다.



- 전. 군.

- 돌. 격. 하. 라.



칠흑색 갑주 아래로 흘러나오는 낮은 음성.

그와 동시에, 때를 기다리고 있던 두 기의 흑귀가 쏘아졌다.

쐐애애액!

새하얀 뼈를 드러낸 유령마가 바람처럼 공간을 가로지르고, 물경 수천에 달하는 광신도들이 그 뒤를 따라 돌격한다.

전장을 뒤흔드는 외침과 함께.



- 천상천하! 만마앙복!

- 천주께서 우리와 함께하신다!



등 뒤에서 울려 퍼지는 그 거대한 함성에, 흑의인은 일순간 등줄기를 타고 솟구치는 짜릿한 전율을 느꼈다.

처음의 계획에서 다소 어긋나긴 했으나, 이제 그런 사소한 문제점 따위는 아무런 상관도 없었다.

자신의 뒤에는 말 그대로의 천군만마(千軍萬馬)가 있었고, 어느덧 절반 가까이 내려온 철교의 뒤에는…….

‘보인다!’

확실했다.

결코 헛것 따위가 아니었다.

쇠사슬로 연결되어 있던 철교가 내려감에 따라 서서히 열리기 시작한 거대한 철문이, 환희에 물든 흑의인의 눈동자에 선명히 비치고 있었다.

츠츠츠츠!

확신에 찬 두 강시술사의 손짓을 따라 요령이 춤추듯 흔들리자, 한계치까지 속도를 끌어올린 괴물들이 동문을 향해 쏘아졌다.

‘할 수 있다.’

느려진 시간 속, 흑의인은 숨을 삼킨 채 시야에 들어온 전장의 상황을 바라보았다.

굉음과 먼지로 뒤덮인 성벽 위에서는 쉴 새 없이 섬광이 번뜩이고, 절반도 넘게 내려온 철교는 해자를 덮고 있다.

이제 남아 있는 거리는, 고작 일백여 장.

‘더, 더 빨리……!’

선두에서 쏘아지는 괴물들의 걸음 소리가 천둥처럼 울려 퍼지고, 두 기의 흑귀를 태운 채 그 옆에서 나란히 내달리는 유령마의 움직임은 흡사 귀신의 그것과도 같았다.

쉬이이익!

세찬 바람이 전신을 휘감는다. 시시각각 좁혀지는 거리에 따라 가슴이 두방망이질 친다.

일백여 장이 반으로.

또 그 반으로.

그리고 마침내.

그그그긍. 쿠웅!

길고 단단한 철교가 해자 위로 내려앉은 순간.

콰아앙!

가장 먼저 철교를 가로지른 두 기의 흑귀를 선두로, 일천의 괴물들이 하나의 거대한 송곳처럼 활짝 열린 성문을 향해 쏟아졌다.

콰드드드드득!

무시무시한 굉음과 함께 피어오르는 흙먼지 속, 마침내 동문이라는 둑을 허물어트린 흑의인과 그 동료는 참았던 숨을 토해 냈다.

해냈다. 그들만의 힘으로.

이는 그 누구도 이견을 제시할 수 없을 만큼 완벽한 성공인 동시에, 실로 혁혁한 전공(戰功)이었다.

설령 그토록 잔인무도한 혈주라 할지라도 인정할 수밖에 없는.

적어도 그 순간만큼은, 두 사람 모두 마음껏 기뻐할 수 있었다.

쉬이잉, 콰앙!

어디선가 날아든 눈부신 강기(罡氣)가, 성문과 철교를 이은 두꺼운 쇠사슬을 단숨에 박살 내버리기 전까지는.

철컥, 드르르륵!

그야말로 순식간이었다. 누구도 반응할 수 없었을 만큼.

“……!”

“……!”

그리고 두 강시술사가 육중한 굉음과 함께 닫히기 시작하는 성문을 멍하니 바라보던 그때, 서서히 가라앉는 먼지구름 너머로 누군가의 흐릿한 인영이 비쳤다.

철퍽. 철퍽.

비틀거리는 걸음걸이. 피에 젖은 도포.

뒤이어 서서히 드러나는 중년의 얼굴과 금기를 범했다는 사실을 증명하듯 붉게 물든 안광.

“……너는.”

흑의인이 무겁게 입술을 뗀 그 순간.

서걱!

불현듯 뻗어 나온 한 줄기의 섬광이 먼지구름과 함께 중년인의, 아니 학수의 목을 가로질렀다.

슬픔과 분노가 뒤섞인 누군가의 음성과 함께.

“대곤륜파의 지엄한 문규(門規)에 따라, 사문의 죄인들을 처단한다.”

털썩, 화아아악.

목을 잃은 육신이 허물어짐과 동시에 좌우로 갈라지는 먼지구름.

그제야 또렷이 보이는 주위의 광경에, 두 강시술사는 비로소 깨달았다.

철교를 내리고 성문을 연 것은, 간자들이 아니라 동문을 지키던 수비군들이었다는 것을.

‘함정……!’

벼락처럼 뇌리를 스치는 두 글자.

그러나 충격도 잠시, 불과 삼천도 되지 않는 수비군들의 숫자와 지친 얼굴을 한 청허자의 모습을 본 흑의인은 입매를 비틀며 웃었다.

“감히 이따위 조잡한 짓거리를 벌이다니.”

이건 함정이지만, 동시에 함정이 아니다.

비록 뒤를 따르던 광신도들은 성문에 가로막혔으나, 정작 가장 강력한 전력인 흑귀와 괴물들은 내부로 진입한 지 오래였으니까.

“고작 이 정도로 우리를 막을 수 있을 것 같더냐.”

그리고 조소 어린 목소리에 대답한 것은, 청허자의 곁에 서 있던 한 청년이었다.

“뭐, 안 될 건 없지. 지금보다 훨씬 더 거지 같은 상황도 많았는데. 다들 안 그래요?”

뭔가 괴롭히고 싶게 생긴 청년의 모습에 흑의인이 눈살을 찌푸린 그때. 면상에 땟국물이 줄줄 흐르는 젊은 거지가 입을 열었다.

“자꾸 거지, 거지 하지 마라. 듣는 거지 기분 나쁘다.”

“네놈은 또 누구…….”

“사실, 매번 이런 상황이긴 했지. 추가 수당으로 얼마를 받아야 할지 가늠조차 안 될 정도야.”

흑의인의 말을 뚝 잘라먹은 냉막한 인상의 청년에 이어, 분위기에 어울리지 않는 맑은 목소리가 울려 퍼졌다.

“하지만 언제나 해냈죠. 모두 함께.”

“맞는 말이긴 하지만, 지금까지와는 다르오. 가장 중요한 한 사람이 빠졌으니.”

“맞다. 태산이. 각주 먹고 싶다. 남 노인도.”

“태산아. 그럴 때는 먹고 싶다가 아니라 보고 싶다고 하는 것이다.”

“아, 헷갈렸다. 역시 주군은 똑똑하다.”

“제법이군. 본녀보다는 못하지만.”

처음 보는 젊은 연놈들에, 척 봐도 많이 모자라 보이는 것 같은 떡대와 산발의 괴인까지.

그 기묘한 광경을 앞에 둔 두 강시술사는 이제 뭐라 되물을 생각조차 들지 않았다.

정확히는, 그럴 가치조차 느끼지 못했다.

“전부 쓸어 버려라.”

그리고 나직한 뇌까림과 함께 요령이 움직이던 그 순간.

부우우우우!

저 멀리서 울려 퍼지는 나팔 소리와 동시에, 동문의 모두가 움직임을 멈췄다.

아니, 그건 누군가에게 있어 희망이요 또 다른 누군가에게 있어서는 더 없는 절망이었다.

“장강수로맹…….”

낮게 가라앉은 누군가의 신음이, 무겁게 공간을 짓눌렀다.
```

## Final English reading copy

```markdown
# Chapter 1117

These days, nowhere in Xining could you find the word peace.

East, west, south, north—not even in the heavens above.

Rain and blood flooded every direction, while screams and crashes rang without pause.

And yet there was one exception: a hill rising tall several hundred jang from the East Gate.

*It’s really coming down out there.*

It was hardly the sort of thought someone in a life-or-death crisis could afford to have.

As he watched the sky pour down thick sheets of rain, as though a giant hole had opened overhead, the black-robed man suddenly turned east.

Whoooosh.

In the deep darkness, waves rippled beneath a fierce wind that swept over them like a storm.

After days of unprecedented rain without a moment’s pause, the place—which had once been a fairly level stretch of ground—had changed so much that it would not have been strange to call it a river.

Of course, that wasn’t what the black-robed man was looking for.

“Have they arrived?”

His companion abruptly asked the question, and the black-robed man answered.

“Not yet.”

“They’re later than expected. They should’ve had plenty of time to get here by now.”

“If they were diligent enough to keep to a schedule, why would they spend their lives robbing people?”

His companion, whose black hood was pulled low, gave a quiet laugh of agreement and continued.

“But I didn’t think they’d be this stupid. Even if they’re nothing but bandits with no proper roots, I thought they’d have at least a little skill or sense if they dared call themselves an Alliance.”

“Maybe this is the result of them thinking things through, in their own way.”

“What do you mean?”

“Even a pack of fools could guess they’d be used as cannon fodder. Most of them are little more than bandits, but their leaders—the Seafaring King and the Green Forest Battle King—know how to think.”

“So they’re deliberately dragging their feet to minimize their losses?”

“The weather’s gotten worse, too, but it’s certainly possible.”

“Even with a full ten thousand of our people keeping watch over those bandits?”

“Who knows? Even if we keep our eyes wide open, those water ghosts of the Yangtze River Channel League might pull something if they’re determined to.”

“Ha. If that’s true, they’re not just stupid. They’re beyond saving.”

At his companion’s clicking tongue, the black-robed man nodded.

He had not said it outright, but there was no one in Dark Heaven who did not know how cruel the Blood Lord could be once he started rampaging with no thought for what came after.

If the combined forces of the Yangtze River Channel League and the Green Forest Alliance arrived only after all the fighting was over…

*After today, the Central Plains will be clean. Not a single bandit in sight.*

But even those bandits still had a chance to survive.

If they arrived in time, before the East Gate opened, and managed to earn at least a little credit to save face, they could extend their tenacious lives just a bit longer.

Of course, that all depended on the Blood Lord’s mood.

*If you want to live, row with every last bit of strength you’ve got. That way, neither of us has to deal with a headache.*

Looking toward the East Gate, where a battle was raging, the black-robed man thought to himself.

What did he care whether a bunch of bandits lived or died? But for someone Dark Heaven classified as a jiangshi sorcerer, it mattered quite a lot.

The black-robed man’s role was less that of a soldier fighting on the battlefield and more like a member of the crew responsible for hauling away the corpses scattered across it.

And while he worried about the excessive workload, the course of the battle around the East Gate—swinging back and forth between attack and defense—was changing abruptly.

BOOOOM!

A deafening crash rang out of nowhere.

The immense noise swallowed not only the sound of the rain but even the thunder that had been striking from time to time. The black-robed man and his companion opened their eyes wide.

At the same moment, they saw the top of the fortress wall collapsing in a flash of light.

“What was that…?”

The black-robed man murmured, almost groaning.

It had lasted only an instant, but he was sure.

Even now, flashes of light were flickering without pause along the wall. He knew that destructive energy was Force.

*Why? We haven’t even pressed the attack. Why would Cheongheoja…?*

The Kunlun Sect Leader’s name flashed through his mind, but the black-robed man soon had to shake his head.

POP! RUMMMBLE!

Another distant flash burst into view.

The light within it was so pale and ominous that it could hardly have come from Daoist martial arts.

“It’s not the Black Ghosts, either. They’re still holding their positions as ordered.”

His companion’s voice came at just the right moment. He was right.

The two Black Ghosts were waiting on the battlefield in front of the wall, along with a considerable number of troops that the Blood Lord had deliberately held back.

“Which means…”

The black-robed man stopped himself.

If the one wielding that Force was neither a Black Ghost nor Cheongheoja, there was only one possibility.

Spies.

The spies they had planted in the Kunlun Sect over many years had finally made their move.

And a step ahead of schedule.

“What do we do?”

At his companion’s question, the black-robed man bit his lip.

It was a real pain in the ass.

The combined forces of the Yangtze River Channel League and the Green Forest Alliance, who should have arrived at the battlefield by now, were still nowhere to be seen. Meanwhile, the spies who were supposed to open the East Gate were caught up in an unexpected fight.

To make matters worse, Ma Sanbao—effectively their direct superior—wasn’t there today. In the end, the black-robed man had to make the call himself.

And he had to do it fast.

In the brief moment that felt like an eternity, the black-robed man stared at the East Gate, beset by a thousand doubts. Then he suddenly opened his eyes wide.

CLANK. GRRRRNNG!

With a heavy grinding sound, the iron bridge began to move slowly.

The massive bridge connected to the moat in front of the gate. It was coming down like a ray of light.

*The iron bridge connects to the gate. That means it can only be operated from inside.*

Then this was clear proof that the spies planted in the Kunlun Sect were opening the gate from within—and a perfect opportunity.

There was no point hesitating any longer.

“I command you: answer the call!”

The black-robed man shouted and pulled the ritual bell from his belt, shaking it with all his might.

Wooooong.

A sinister sound carried on the wind, sending a wave of force outward.

At the same time, the hill they had been standing on—or rather, the enormous masses of flesh that the rain and chaos made impossible to distinguish from a hill—answered the force.

GRRRRKK!

The ground shook as if an earthquake had struck. A horrible corpse stench rose from the rain-soaked earth and mud.

BOOM. BOOOOM!

The monsters shook off the mud plastered all over their bodies and rose to their full height on limbs as thick as tree trunks. There were a thousand in all.

Perched on the shoulder of one of them, the black-robed man shook his ritual bell once more and whispered:

“Wipe them all out.”

At that instant—

—KROOOAAAR!

With a roar as immense as their bodies, a thousand monsters surged toward the battlefield like a wave.

THUDDUDDUDDUD!

Was this what it would look like if the Yellow River flooded?

Screams rose belatedly from the wall as the monsters came charging in with a ferocious momentum no one could stop. But they weren’t the only enemies the defenders had to face.

—All. Troops.

—Charge.

A low voice emerged from beneath black armor.

At the same time, the two Black Ghosts who had been waiting sprang into action.

SHWOOOSH!

A ghost horse, its white bones exposed, raced forward like the wind, with several thousand fanatics charging behind it.

A roar that shook the battlefield rang out.

—Heaven above and earth below! Let ten thousand demons bow in homage!

—The Lord of Heaven is with us!

At the immense war cries from behind him, the black-robed man felt a thrilling shiver run up his spine.

Things had strayed a little from the original plan, but now such minor setbacks didn’t matter.

He had a literal army at his back. And behind the iron bridge, which had now descended nearly halfway…

*I see it!*

There was no doubt.

He wasn’t seeing things.

As the iron bridge lowered on its chains, the enormous iron gate began to open. The sight was clear in the black-robed man’s eyes, brimming with delight.

Tss-tss-tss-tss!

The two jiangshi sorcerers waved their hands with confidence, and the ritual bell danced in the air. The monsters, moving at full speed, shot toward the East Gate.

*We can do this.*

As time seemed to slow, the black-robed man held his breath and watched the battlefield.

Flashes of light flickered without pause atop the wall, which was shrouded in crashes and dust. The bridge, more than halfway down, now covered the moat.

The remaining distance was only a little over a hundred jang.

*Faster. Faster…!*

The monsters leading the charge thundered forward, their footsteps like thunderclaps. Beside them, the ghost horse carrying the two Black Ghosts galloped as if it were a specter.

Whoooosh!

A fierce wind wrapped around him. As the distance closed by the second, his heart pounded harder.

A little over a hundred jang became half.

Then half of that.

And at last—

GRRRNNG. BOOM!

The long, sturdy iron bridge came down over the moat.

BOOOOM!

Led by the two Black Ghosts, who crossed the bridge first, a thousand monsters surged toward the wide-open gate like one enormous spear.

KRRRRRUNCH!

Amid a terrifying crash and a cloud of dust, the black-robed man and his companion—who had finally broken through the East Gate’s defenses—let out the breaths they had been holding.

They had done it. By their own strength.

It was a flawless success, one no one could dispute—and a truly remarkable feat.

Even the merciless Blood Lord would have to acknowledge it.

At least for that moment, both men could rejoice to their hearts’ content.

SHWING—BOOM!

Until a dazzling flash of Force flew in from somewhere and shattered the thick chain connecting the gate to the iron bridge.

CLANK. RRRRRK!

It happened in an instant. No one could react in time.

“……!”

“……!”

As the two jiangshi sorcerers stared blankly at the gate, which had begun to close with a heavy crash, a hazy silhouette appeared beyond the dust cloud as it slowly settled.

SPLASH. SPLASH.

A staggering gait. A robe soaked in blood.

Then a middle-aged face gradually came into view, its eyes glowing red—the proof that he had committed a forbidden act.

“……You.”

The black-robed man slowly parted his lips.

At that moment—

Slice!

A streak of light suddenly shot out, slicing through the dust cloud and the middle-aged man’s—no, Hak Su’s—neck.

A voice, thick with sorrow and anger, followed.

“By the solemn rules of the Great Kunlun Sect, I will execute the traitors of our sect.”

THUD. FWOOSH.

As the headless body collapsed, the cloud of dust split apart.

Only then could the two jiangshi sorcerers clearly see what was around them. They finally understood.

It was not the spies who had lowered the bridge and opened the gate. It was the defenders who had been guarding the East Gate.

*A trap…!*

The realization flashed through their minds like lightning.

But the shock lasted only a moment. Seeing that there were fewer than three thousand defenders and that Cheongheoja looked exhausted, the black-robed man twisted his lips into a grin.

“You dare pull a shoddy trick like this?”

It was a trap—but at the same time, it wasn’t.

The fanatics following them had been blocked by the gate, but the most powerful forces—the Black Ghosts and the monsters—had already entered.

“Did you think you could stop us with this?”

A young man standing beside Cheongheoja answered his scornful question.

“Why not? We’ve had plenty of situations a whole lot worse than this. Right, everyone?”

At the sight of the young man, who looked like he’d be fun to torment, the black-robed man frowned. Just then, a young beggar, grime streaming down his face, spoke up.

“Quit calling me a beggar. It hurts the feelings of the beggar listening.”

“Who the hell are you…?”

“Honestly, we’ve been in this situation every time. I can’t even begin to figure out how much extra pay we should be getting.”

A young man with a cold expression cut the black-robed man off, followed by a clear voice that didn’t fit the mood at all.

“But we always make it through. Together.”

“That’s true, but this time’s different. The most important person isn’t here.”

“Right. Taishan wants to eat Pavilion Master. Old Man Nam, too.”

“Taishan. You mean you miss them, not that you want to eat them.”

“Oh, I got mixed up. Lord is smart, as expected.”

“Not bad. Still, not as good as me.”

The two jiangshi sorcerers had never seen these young men and women before. There was also a hulking man who looked none too bright, and a wild-haired eccentric.

Faced with the bizarre scene, the two sorcerers couldn’t even think of what to ask.

More precisely, they didn’t think it was worth asking.

“Wipe them all out.”

The ritual bell began to move with his quiet mutter.

Boooooo!

At the sound of a horn from far away, everyone at the East Gate stopped moving.

No—some heard it as hope; for others, it was the greatest despair.

“The Yangtze River Channel League…”

Someone’s low groan pressed heavily on the space around them.
```
