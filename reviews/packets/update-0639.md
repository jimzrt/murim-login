<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0639.txt",
      "sha256": "ee35037e93e946463f77e4fd9cd4080632780e5ec30415e762fef0f0cbf37ff4",
      "bytes": 12615
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "122f1910dc514a334363cb19cb4d2e1e0af8bc7827b85599c6af88bd22a43781",
      "bytes": 1363
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a6b72faf490a40872bc1f900a4f279b61f1b7e074dc49b6249dd1da3312b72ad",
      "bytes": 197213
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "ad77acbb22f9c41f31e80c24d6365238fafeda071d2bbaeca5a5e3a33bd4cdd7",
      "bytes": 560
    },
    {
      "path": "characters/Hwangso.md",
      "sha256": "08a3f0196e51ea3f4e8362673cbda0856b8578d73eec105d8c50a9b8a1a82691",
      "bytes": 698
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "c8c5e296da003a1e662f53faa7a5d15a6c61b905890c5290d06bed8a71d8addf",
      "bytes": 1702
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "6b492600b65eb011a1e343441c229de2fa914402a26a7ce1370ff0ede97868b1",
      "bytes": 528
    },
    {
      "path": "characters/Yayul Cheok.md",
      "sha256": "50bda3bf7f71e84bf2cd43b18790629aea0cea9064a75d7cf8b39fb4a9dda30e",
      "bytes": 912
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2ee77e9a1d5d7d04bc6461137b6bdb37bcf4edf48b220c849a97822225533a4e",
      "bytes": 202599
    }
  ],
  "estimated_tokens": 9816
}
-->

# Durable State Update — Chapter 639

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 639. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 639. Profile updates may replace only one
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
  "chapter": 639,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 639,
    "continuity_sources": [639],
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
    "Jin Taekyung and the Beast Miao King are pursuing the last surviving Thousand-Year Spider in the Poisonblood Grounds.",
    "The inner Poisonblood Grounds remain filled with Poison Mist and dangerous life-forms.",
    "Thousand-Year Spiders are cunning Nanman venomous beasts with acidic slime and potentially thousand-year lifespans.",
    "Jin's White Flame spear is empowered by Scorching Yang Qi and can kill Thousand-Year Spiders.",
    "Jin has earned the Indiscriminate Hunting Bug achievement, granting additional stats against insect-form enemies."
  ],
  "continuity_sources": [
    638
  ],
  "open_questions": [
    "What lies beyond the unseen spiderweb toward which the last Thousand-Year Spider fled?",
    "Where is the Thousand-Year Spider leading Jin Taekyung and the Beast Miao King?",
    "What further dangers are hidden deeper in the Poisonblood Grounds?"
  ],
  "safe_through": 638,
  "temporary_decisions": [
    "Use Hope goshiwon for 희망 고시원.",
    "Use ghost spider for 유령거미, Joro spider for 무당거미, Brazilian wandering spider for 브라질 떠돌이 거미, and tarantula for 타란툴라.",
    "Use Indiscriminate Hunting Bug for the achievement 가리지 않는 사냥충.",
    "Use Inventory and Summon for the System commands 인벤토리 and 소환."
  ],
  "version": 1
}
```

## Exact glossary matches

| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 남만야수궁  | **Nanman Beast Palace**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 신법     | **movement technique**                           |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 마교     | **Demonic Cult**                                 |                                                       |
| 일격     | **One Strike**                         |
| 지능               | **Intelligence**               |
| 헌터      | **Hunter**            |
| 정마대전   | **Great Faction War**         |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 황소 | **Hwangso** | First-generation disciple of the Gongdao Sect and a reluctant search-party member. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 야율척 | **Yayul Cheok** | Beast Miao King and lord of the Nanman Beast Palace. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 권기 | **Fist Energy** | Projected martial energy produced by a fist technique. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 소평 | **So Pyeong** | Alliance office worker assigned to prepare a report. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 백족 | **Bai people** | Ethnic group encountered in Yeongin. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 흑호 | **Black Tiger** | A colossal black tiger that appears at the Ailao Mountain massacre site. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 독무 | **Poison Mist** | Deep green mist covering the Poisonblood Grounds swamp. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 천년지주 | **Thousand-Year Spider** | Monster appearing at the end of the chapter. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 야율척 | 태산 | Palace_Lord_to_Fire_Dragon_Pavilion_member | you | puzzled and blunt | Yayul Cheok asks Taishan, standing beside Hwaran, to identify him, receiving only Taishan's declaration that he is hungry. |
| 야수묘왕 | 흑호 | hostile pursuer to unknown supernatural beast | you | blunt and furious | Directly challenges the Black Tiger over the massacre. |

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 638
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, and a master among the Ten Kings.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace and is responsible for the forces stationed at Ailao Mountain.

### Hwangso.md

# Hwangso (황소)

- **Safe through:** Chapter 607
- **Aliases:** None
- **Role:** First-generation disciple of the Gongdao Sect in Sichuan, deployed with roughly thirty second- and third-generation disciples to search for the surviving Third Fiend.
- **Personality:** Privileged, impatient, pleasure-seeking, inattentive, and dismissive of the danger surrounding the mission.
- **Voice:** Complaining and casual, with irreverent sarcasm toward his Senior Brother and the search.
- **Relationships:** His Senior Brother supervises him, and his prosperous merchant father forced him into the Murim to establish family connections.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 635
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 637
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord.

### Yayul Cheok.md

# Yayul Cheok (야율척)

- **Safe through:** Chapter 633
- **Aliases:** Beast Miao King
- **Role:** Yayul Cheok is the over-eighty Beast Miao King, lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, and great chieftain representing the Miao people.
- **Personality:** Boisterous, warmhearted, forthright, playful, and politically conscious of the tribal coalition he leads.
- **Voice:** Rough, loud, convivial, and teasing, becoming authoritative when discussing Nanman's laws or political decisions.
- **Relationships:** Jeok Cheongang is an old acquaintance whom he respects; Baeksang is his sworn younger brother and childhood companion, and they fought together during the Great Faction War; Yayul Mok serves as his Young Palace Lord; Jin Taekyung is Jeok's Disciple whom he welcomes into the Nanman Beast Palace.

## Korean source

```text
＃639화



생각해 보면 당연한 일이다.

천년지주(千年蜘蛛)가 아무리 대단한 독물이라고 해도 그 본질은 결국 거미였다.

놈들의 본거지나 다름없는 독혈지 곳곳에는 거미줄이 지천으로 깔려 있었고, 천년지주 오 남매의 마지막 생존자는 완전히 전의를 상실한 채 거미줄을 타고 도주하는 중이었다.

그리고 이 상황에서 한 가지 예측하지 못했던 건…….

퉁! 쉬쉬쉬쉭!

저 거대한 거미 놈이 도망치는 속도가, 생각 이상으로 훨씬 빨랐다는 거다.

‘……아니, 뭔데 저렇게 빨라.’

놈이 필사적으로 도망치는 중이기 때문인지, 그도 아니면 만일을 대비하여 거미줄을 곳곳에 깔아 두어서인지는 모르겠다.

하지만 무슨 이유에서건 천년지주와의 거리는 좀처럼 좁혀지지 않았고, 수십여 장 위의 허공과 거목 사이를 오가며 도망치는 놈을 잡을 방법은 마땅치 않았다.

‘스파이더맨이 괜히 빠른 게 아니었…….’

내심 중얼거리며 경신법을 펼치던 그 순간. 전신을 엄습하는 알 수 없는 한기에 나는 본능적으로 머리를 숙였다.

사각!

예리한 절삭음과 함께 한 움큼이나 잘려 나간 머리카락이 허공에 흩날린다.

아슬아슬하게 스쳐 지나간 그것의 정체는 다름 아닌 거미줄이었다.

철사만큼이나 단단하고 탄력을 지닌 그것이 가파른 속도를 만나 예리함을 지니게 된 것이다.

“야율 대협!”

그 사실을 깨닫자마자 경고를 담아 외쳤지만, 나보다 체격이 크고 움직임이 거친 야수묘왕의 대처는 늦은 감이 있었다.

서걱!

뭐지. 면도기 CF를 본 것 같은데.

살과 뼈 대신 정수리가 깔끔하게 밀린 야수묘왕이 처참한 표정으로 대답했다.

“……왜 불렀느냐.”

“……아닙니다. 그냥 불러 봤어요.”

풍성한 사자 갈기처럼 휘날리던 머리카락은 더 이상 찾아볼 수 없다.

산성을 듬뿍 머금은 천년지주들의 가래 세례와 거미줄에 의해 잘려나간 야수묘왕의 정수리는 막 뭍으로 올라온 문어처럼 번쩍 빛나고 있었다.

‘닥터 옥토퍼스와 스파이더맨의 대결인가.’

선악이 뒤바뀐 것 같긴 하지만 어쨌든.

히어로 영화의 한 장면을 직관하고 있다고 생각하자 가슴이 웅장해진다.

물론 그와는 반대로 머리숱이 조촐해진 문어묘왕의 분노는 하늘을 찔렀다.

“놈! 감히!”

당연하게도 그가 분노하는 이유는 머리숱 때문만이 아니었다.

제각각 다른 부족이라고는 하나, 하루아침에 백성이나 다름없는 수백여 명의 전사들을 잃은 그다. 벌겋게 달아오른 눈가로부터 광포한 기운이 흘러넘쳤다.

콰아앙!

야수묘왕이 거세게 발을 구른 순간, 독과 습기로 눅눅한 지면이 싱크홀처럼 움푹 주저앉는다.

동시에 막대한 반탄력을 이용하여 높게 뛰어오른 그가 일권을 내질렀다.

후우웅, 파앙!

압축된 공기가 터져나가고 바람이 물결쳤다.

공간을 가르며 발출 된 권기(拳氣)가 어둠에 녹아든 거미줄을 끊으며 천년지주를 향해 쏘아졌다.

쐐애애액! 쉭!

하지만 나와 야수묘왕의 바람과는 달리 발출된 권기는 허공을 갈랐고, 아슬아슬하게 죽음의 위기에서 벗어난 천년지주는 소름 끼치는 울음소리를 토해 냈다.

- 시시시시싯!

그것은 평범한 울음소리가 아니었다.

마치 전음(傳音)처럼 귓속을 파고드는 기이한 소음이 공간을 울리며 퍼져 나가자, 날 선 감각으로 수많은 움직임들이 느껴졌다.

‘이건.’

사사삭.

독혈지를 죽음의 땅으로 변모시킨 독무(毒霧)와 검게 물든 풀숲.

나이를 짐작하기 어려운 거목들 사이에서 모습을 드러낸 ‘그것들’의 모습에, 나는 잠시 잊고 있었던 한 단어를 떠올렸다.

‘독물의 왕.’

천년지주를 가리키는 그 표현은 짧고 정확했다.

독혈지 곳곳에 웅크린 채 명령을 기다리던 독물들은 마침내 왕의 부름에 답했고, 무수한 숫자의 군세가 되어 나와 야수묘왕의 앞길을 가로막고 있었다.

스륵. 스스슥!

채찍처럼 길고 커다란 뱀과 지네. 사람의 머리만 한 거미와 두꺼비. 거목의 잎사귀 어딘가에서 흘러나온 수백 마리의 벌떼까지.

도무지 종류를 알 수 없는, 그리고 알고 싶지도 않은 흉측한 모습을 한 독물들이 서로를 향해 뭉치고 잇는다.

눈 깜짝할 새에 수십에서 수백이 되고, 수백은 수천으로 불어나 마침내 하나의 벽을 완성시켰다.

콰아아아!

오직 한 길로 이어진 독혈지를 가로막고, 거대한 삼각파도가 되어 덮쳐오는 무수한 독물들.

그리고 훨씬 낮아진 허공에서 거미줄을 밟은 채 우리를 내려다보는 천년지주.

더 이상 도망치지 않고 왕처럼 지상을 굽어보는 놈의 모습에, 나는 작게 중얼거렸다.

“씨벌놈. 이제와서 멋있는 척은.”

처음부터 이것을 노린 것이 틀림없다.

남만은 확실히 염병할 땅이다. 무슨 놈의 짐승이며 거미가 이렇게 교활한지.

애뇌산의 망령이라는 흑호를 따라 독혈지에 진입했고, 그곳에서 만난 천년지주는 자신에게 유리한 전장에 도달하자 마침내 모든 호위병들을 불러 모았다.

지금까지 직접 겪은 것만 해도 어지간한 인간에 비교해도 결코 떨어지지 않는 수준의 지능이다.

‘특히 어떤 식충이 놈에 비하면 아인슈타인이지.’

문득 태산을 떠올린 나는 야수묘왕을 향해 고개를 돌렸다.

남만에서 일평생을 살아온 그로서도 처음 보는 광경인지, 얕은 침음성을 흘린 그는 나와 눈이 마주치자 굳은 표정으로 입을 열었다.

“겁먹을 필요 없다. 나도, 너도 이곳에서 죽지 않을 테니.”

겁?

나는 대답 대신 피식 웃었다.

아마 저것보다 나와 거리가 가까우면서도, 먼 단어도 찾기 힘들 거다.

돌이켜 보면 나는 늘 겁이 많다고 생각했는데, 막상 죽음의 위기 앞에서는 단 한 번도 물러선 적이 없었으니까.

‘처음에는 겁이 없어서 헌터가 됐고, 나중에는 겁이 많아서 무공을 익혔지.’

참 희한한 일이다. 죽는 것이 두려워서 온 힘을 다해 발버둥 쳤던 주제에, 늘 죽어도 이상하지 않을 전장을 향해 나아간다는 것이.

하지만…… 적어도 오늘만큼은, 난 죽지 않을 것 같다.

콰아아아아!

넘실거리며 가까워지는 독물들의 파도를 바라보며, 나는 불쑥 입을 열었다.

“저것들이 사라지면, 그 즉시 놈을 죽이십시오. 아니다. 딱 숨이 끊기지 않을 정도로만.”

“뭐?”

“명심하세요. 조금이라도 지체하면 안 됩니다. 방심한 채 높이를 낮춘 지금 처리해야 해요.”

“그게 무슨…….”

지금.

나는 야수묘왕의 반문에 대답하는 대신 부드럽게 지면을 밟았다. 단전에서 솟구친 공력은 이미 발끝을 향해 치달리는 중이었다.

스륵. 쾅!

압축. 그리고 폭발.

발끝이라는 일점(一點)에서 터져나간 공력이 내 전신에 빛살과도 같은 속도를 선물한다. 동시에 일진광풍이 온몸을 휘감고 진녹색의 독무가 흩어졌다.

그리고 그 너머에, 수천 마리에 달하는 독물들이 만들어 낸 거대한 벽이 나를 기다리고 있었다.

콰아아아!

머리 위로 드리워지는 짙은 그늘.

가뜩이나 어두운 독혈지가 완전한 어둠에 잠긴 그 순간. 내 손에 들린 백염(白炎)의 창날로부터 휘황한 빛이 터져 나왔다.

우우웅.

흡사 벌떼가 우는 소리와 함께 하늘보다 푸르른 화염이 깃든다.

삼 갑자에 달하는 강대한 열양지기가 서로를 끌어당기고, 잇고, 뭉치며 더욱 거대한 겁화(劫火)로 화한다.

그리고 그 끝에.

‘일섬(一殲).’

구구구구궁!

어둠을 찢고 땅과 하늘마저 떨어 울리는, 섬광과 굉음이 있었다.



* * *



야수묘왕 야율척은 어릴 적부터 스스로를 야인(野人)이라고 생각했다.

예의범절과 고상한 태도과는 거리가 먼, 거칠기 짝이 없는 날 것 그대로의 사람.

하지만 자리가 사람을 만든다고 했던가.

살다 보니 앞장서서 책임져야 할 일도. 뭐 하나 볼 것 없는 자신을 따르는 이들도 생겼다.

거침없이 흐르는 세월 속에 그는 어느덧 백족의 대족장이 되었고, 문득 주위를 둘러보니 남만야수궁의 궁주라는 막중한 자리에 올라 있었다.

‘어쩌다가 이렇게 된 거지?’

도무지 알 수 없는 일이었다.

일평생 무공만 수련했을 뿐인데 일이 이렇게 될 줄이야.

하지만 이미 오래전에 엎질러진 물이었다. 돌이키기에는 늦었고, 주워 담기는 불가능했으니 그는 궁주의 책무에 최선을 다했다.

누군가를 두들겨 패는 일도 없어졌고, 숨 쉬는 것보다 자연스럽던 욕설도 줄였다.

말귀를 더럽게 못 알아 처먹는 부족장의 귓방망이를 후려친다면 마음의 평안을 얻을 수 있겠지만, 이제는 귀가 영영 안 들리게 될 그 부족장이 남만야수궁에 반기를 들 테니까.

하지만 오랜 궁주 생활로 훨씬 얌전해진 야수묘왕의 입술도, 눈앞에서 펼쳐진 광경을 목격한 순간 저절로 움직이기 시작했다.

“어어, 저게 씨벌 뭐여. 어어어.”

구구구궁!

모든 것이 부서지고, 녹아내린다.

수천 마리로 이루어진 독물의 파도가, 그의 눈앞에서 산산이 부서지고 있었다.

심심하면 곰을 사냥하는 쌍두각사(雙頭角蛇)도. 한 방울의 독으로 백 마리의 황소를 죽이는 흑와(黑蛙)도. 반 각이면 호랑이를 뼈만 남기고 발라먹는다는 금봉(金蜂)도.

화륵. 콰아아아아!

그 흉측함만큼이나 강한 힘을 지닌 수천 마리의 독물이, 어둠을 밝힌 푸른 화염와 굉음 앞에 잿더미로 화하고 있었다.

‘……이런 미친.’

정마대전 이후 장장 오십여 년만이었다. 이런 경악스러운 광경은.

그토록 강했던 마교의 검마(劍魔)가 죽기 직전 펼쳤던 최후의 절초도 눈앞의 광경에 비할 수는 없었고, 그런 검마의 마지막 일격을 손쉽게 피하고 죽기 직전까지 자근자근 짓밟은 화왕(火王) 적천강조차 이 정도의 파괴력을 보여 준 적은 없었다.

물론 이런 생각을 하는 그. 야수묘왕 야율척조차도 마찬가지다.

‘도대체 어떻게.’

숨길 수 없는 경악과 의문. 부릅뜬 눈으로 타오르는 겁화 앞에 우뚝 선 청년의 뒷모습을 바라보던 야수묘왕은, 불현듯 뇌리를 스치는 한 마디를 떠올렸다.



‘저것들이 사라지면, 그 즉시 놈을 죽이십시오. 아니다. 딱 숨이 끊기지 않을 정도로만.’



“……!”

처음에는 무슨 헛소리를 지껄이나 싶었는데, 그 헛소리가 현실이 되어 버렸다.

동시에 야수묘왕은 자신이 무엇을 해야 하는지 깨달았다.

쾅!

굉음과 함께 하늘을 향해 솟구치는 신형. 비록 야수묘왕의 움직임은 반 박자 늦었지만, 그것은 도저히 예측할 수 없던 상황을 맞이한 천년지주 역시 마찬가지였다.

- 시, 시싯?

혼란스러운 듯, 제각기 다른 방향으로 움직이던 크고 작은 여러 개의 눈동자가 야수묘왕을 발견하고 우뚝 멈춘 순간.

얼마 남지 않은 머리카락을 흩날리며 날아오른 그의 입가에 서늘한 웃음이 맺혔다.

“드디어 잡았다. 이 찢어 죽일 놈.”

- ……!

천년지주가 저지른 결정적인 패착은 두 가지였다.

첫째. 젊은 인간의 힘을 과소평가한 것.

둘째. 늙은 인간의 부족민들을 죽이고, 그가 평소 자랑스럽게 여기던 풍성한 머리카락을 밀어 버린 것.

촤아악!

마지막 저항으로 내뿜은 점액질은 허공을 갈랐고, 야수묘왕이 뻗은 손은 천년지주의 다리를 잡았다.

콰득!

- 시이이이잇!

천년지주는 다리가 뽑혀 나가는 통증과 함께, 비명을 내지르며 땅으로 추락했다.
```

## Final English reading copy

```markdown
# Chapter 639

When you thought about it, it was only natural.

No matter how extraordinary a Thousand-Year Spider was as a venomous creature, its essence was still that of a spider.

Spiderwebs were spread everywhere throughout the Poisonblood Grounds, practically their home territory, and the last survivor of the five Thousand-Year Spider siblings had completely lost the will to fight and was fleeing along its webs.

And there was one thing I hadn’t expected in this situation…

*Thump! Shhhhk!*

That enormous spider was much, much faster than I had imagined.

*……What the hell? Why is it so fast?*

I didn’t know whether it was because the creature was fleeing for its life or because it had laid webs everywhere in preparation for emergencies.

Whatever the reason, the distance between us and the Thousand-Year Spider hardly narrowed at all, and I had no good way to catch it as it fled back and forth between the air dozens of zhang above us and the great trees.

*No wonder Spider-Man was so fast……*

I was muttering inwardly as I used my movement technique when an inexplicable chill swept over my entire body. I instinctively ducked my head.

*Slice!*

With a sharp cutting sound, a handful of hair drifted through the air.

The thing that had narrowly grazed past me was none other than a spiderweb.

It was as tough and elastic as steel wire, and striking it at such high speed had turned it into a razor-sharp edge.

“Great Hero Yayul!”

The moment I realized that, I shouted a warning, but the Beast Miao King’s response was a little late. He was larger than me, and his movements were rougher.

*Slice!*

*What is this? I feel like I’ve seen a razor commercial.*

Instead of flesh and bone, the top of the Beast Miao King’s head had been shaved clean. He answered with a miserable expression.

“……Why did you call me?”

“……Nothing. I just felt like calling you.”

The thick hair that had once streamed behind him like a lion’s mane was nowhere to be seen.

The Beast Miao King’s crown, stripped bare by the Thousand-Year Spiders’ barrages of acid-laden phlegm and their webs, gleamed like an octopus that had just come ashore.

*Is this a battle between Doctor Octopus and Spider-Man?*

The sides seemed to be reversed, but still.

Thinking of it as watching a scene from a superhero movie made my heart swell with grandeur.

Of course, the octopus Miao King’s anger over his now-sparse hair was reaching the heavens.

“You bastard! How dare you!”

Naturally, his hair wasn’t the only reason he was angry.

They might have belonged to different tribes, but he had lost hundreds of warriors who were practically his own people overnight. A savage energy flowed from the corners of his reddened eyes.

*Kra-boom!*

The moment the Beast Miao King stamped his foot, the damp ground, saturated with poison and moisture, sank inward like a sinkhole.

At the same time, he used the tremendous rebound force to leap high into the air and threw a punch.

*Whoooom! Bang!*

Compressed air burst apart, and the wind rippled.

The Fist Energy released as it tore through space severed the webs that had melted into the darkness and shot toward the Thousand-Year Spider.

*Shreeeek! Shhk!*

But contrary to what the Beast Miao King and I had hoped, the projected Fist Energy cut through empty air, and the Thousand-Year Spider, having narrowly escaped death, let out a chilling cry.

—Ssssssissss!

It wasn’t an ordinary cry.

A strange noise that burrowed into my ears and spread through the space like Sound Transmission caused countless movements to register in my sharpened senses.

*This is……*

*Rustle.*

The Poison Mist that had transformed the Poisonblood Grounds into a land of death.

The grass stained black.

Between the great trees whose ages were impossible to guess, *those things* emerged into view, and I recalled a word I had momentarily forgotten.

*King of the venomous beasts.*

It was a short and accurate expression for the Thousand-Year Spider.

The venomous beasts that had crouched throughout the Poisonblood Grounds, waiting for orders, had finally answered their king’s call. They had become an army of countless creatures and were blocking the path ahead of the Beast Miao King and me.

*Slither. Ssssss!*

Snakes and centipedes as long and enormous as whips. Spiders and toads the size of human heads. Hundreds of bees pouring out from somewhere among the leaves of the great trees.

Venomous beasts with hideous forms I couldn’t identify—and didn’t want to identify—were converging and joining together.

In the blink of an eye, dozens became hundreds. Hundreds became thousands. At last, they formed a single wall.

*Kraaaaa!*

The countless venomous beasts blocked the only path through the Poisonblood Grounds and surged toward us as a gigantic triangular wave.

And above them, at a much lower height than before, the Thousand-Year Spider stood on its web and looked down at us.

It no longer fled. Now it gazed down upon the ground like a king.

Looking at it, I muttered under my breath.

“Fucking bastard. Acting cool now, are you?”

It had clearly been aiming for this from the beginning.

Nanman really was a goddamn place. What kind of animals and spiders were this cunning?

I had entered the Poisonblood Grounds following the Black Tiger known as Ailao Mountain’s Wraith. The Thousand-Year Spider we encountered there had finally summoned all its guards once it reached a battlefield favorable to itself.

Judging by everything I had seen firsthand, its intelligence was in no way inferior to an ordinary human’s.

*Compared to some glutton, it’s Einstein.*

Taishan suddenly came to mind, and I turned toward the Beast Miao King.

Even for a man who had lived his entire life in Nanman, this seemed to be a sight he had never seen before. He let out a low groan, and when our eyes met, he spoke with a solemn expression.

“There is no need to be afraid. Neither you nor I will die here.”

Afraid?

Instead of answering, I let out a quiet laugh.

It would be hard to find another word that was both closer to me and farther from me than that one.

When I thought about it, I had always considered myself a coward. Yet when faced with the threat of death, I had never once backed down.

*At first, I became a Hunter because I wasn’t afraid. Later, I learned martial arts because I was afraid.*

It was a strange thing. I had fought and struggled with all my strength because I was afraid of dying, yet I kept heading toward battlefields where it wouldn’t have been strange for me to die at any moment.

But……at least today, I didn’t think I would die.

*Kraaaaaaaaa!*

As I watched the wave of venomous beasts roll closer, I suddenly opened my mouth.

“When those things are gone, kill it immediately. No—just hurt it enough to leave it barely breathing.”

“What?”

“Remember this. You cannot delay even a little. We need to deal with him now, while he’s lowered his height without suspecting anything.”

“What are you talking abou—”

Now.

Instead of answering the Beast Miao King’s question, I lightly touched the ground. The internal energy surging from my dantian was already racing toward my toes.

*Slither. Boom!*

Compression.

And then, an explosion.

The internal energy that burst from a single point—the tip of my toe—gave my entire body the speed of a beam of light. At the same time, a fierce gale wrapped around me and scattered the deep green Poison Mist.

Beyond it, a colossal wall formed by thousands of venomous beasts was waiting for me.

*Kraaaaaa!*

A thick shadow fell over my head.

The Poisonblood Grounds were already dark, but at that moment, they sank into complete darkness.

Then brilliant light burst from the blade of the White Flame spear in my hand.

*Vooooom.*

Along with a sound like a swarm of bees, flames bluer than the sky began to burn.

Three jiazi’s worth of powerful Scorching Yang Qi drew together, linked, and coalesced, transforming into an even greater hellfire.

And at the end of it all—

*One Annihilation.*

*Ruuuumble!*

A flash and a roar tore through the darkness, making even the earth and sky tremble.

* * *

Beast Miao King Yayul Cheok had thought of himself as a wild man since childhood.

He was a raw, rough person, as far removed from etiquette and refined manners as one could get.

But they said a position made the person.

As he lived, he found himself with responsibilities that had to be shouldered from the front. He also found people who followed him despite there being nothing worth admiring in him.

As the years flowed relentlessly onward, he eventually became the great chieftain of the Bai people. Then one day, he looked around and found himself sitting in the weighty position of Palace Lord of the Nanman Beast Palace.

*How did this happen?*

He had no idea.

He had only trained in martial arts his entire life. How had things ended up like this?

But the water had been spilled long ago. It was too late to turn back, and impossible to scoop it up again, so he did his best to fulfill his duties as Palace Lord.

He no longer beat people up.

He also cut down on the profanity that had once come as naturally as breathing.

If he smacked the ears of a tribal chieftain who was unbelievably incapable of understanding what he was told, he could find peace of mind—but by now, that chieftain would rise in rebellion against the Nanman Beast Palace after being rendered permanently deaf.

But even the lips of the Beast Miao King, who had become much tamer through his long years as Palace Lord, began to move on their own when he witnessed the sight unfolding before his eyes.

“Uh, what the fuck is that? Uhhh.”

*Ruuuumble!*

Everything was breaking apart and melting.

The wave of thousands of venomous beasts was shattering to pieces right before his eyes.

The two-headed horn snake that hunted bears whenever it grew bored. The black frog that could kill a hundred bulls with a single drop of poison. The golden bees said to strip a tiger down to its bones in half a gak.[^1]

[^1]: A traditional East Asian unit of time, roughly equivalent to seven and a half minutes.

*Fwoosh! Kraaaaaa!*

Thousands of venomous beasts whose strength matched their hideousness were turning to ash before the blue flames and the roar that lit up the darkness.

*……This is insane.*

It had been more than fifty years since the Great Faction War.

That was how long it had been since he had witnessed a scene this astonishing.

Even the final ultimate technique unleashed by the Demonic Cult’s Sword Demon just before his death could not compare with the sight before him. And even Fire King Jeok Cheongang, who had easily dodged the Sword Demon’s final strike and methodically trampled him until he was on the verge of death, had never displayed this level of destructive power.

Of course, that applied to the man having these thoughts as well.

Even Beast Miao King Yayul Cheok himself.

*How is this possible?*

Unable to hide his shock and confusion, the Beast Miao King stared at the back of the young man standing tall before the blazing hellfire.

Then a single sentence suddenly flashed through his mind.

> *“When those things are gone, kill him immediately. No. Just don’t let him stop breathing.”*

“……!”

At first, he had wondered what kind of nonsense Jin Taekyung was spouting.

But that nonsense had become reality.

At the same time, the Beast Miao King realized what he needed to do.

*Boom!*

His body shot toward the sky with a thunderous roar.

Although the Beast Miao King’s movements were half a beat late, the same was true of the Thousand-Year Spider, which had been confronted with a situation it could never have predicted.

—S-Siss?

Several large and small eyes moved in different directions as though confused. Then they spotted the Beast Miao King and stopped.

A cold smile formed at the corner of his mouth as he flew upward, his remaining hair streaming behind him.

“I’ve finally caught you. You piece of shit. I’ll tear you apart.”

—……!

The Thousand-Year Spider had made two fatal mistakes.

First, it had underestimated the young human’s strength.

Second, it had killed the old human’s tribespeople and shaved off the thick hair he had always been proud of.

*Splaaash!*

The slime it spat out in one last act of resistance cut through the air, while the Beast Miao King’s outstretched hand caught one of the Thousand-Year Spider’s legs.

*Crack!*

—Siiiiiiit!

With the pain of its leg being ripped out, the Thousand-Year Spider let out a scream and plummeted toward the ground.
```
