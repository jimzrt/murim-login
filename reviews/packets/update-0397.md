<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0397.txt",
      "sha256": "b0bd7274adae4e9bbae1f08377a61d7977a1abc863a3d7091b19f00dbde01d7d",
      "bytes": 17396
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c1d569035451ec31f65268b68a12d3910a262687ddb6b3b8533563c2d725b67b",
      "bytes": 2800
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "89060d8deb1aecc1feaa715fa00524cd58dd7dfd97dcd08d1c5d706e79dfeaef",
      "bytes": 135344
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f5ea964445187a61a8df27e8d1492436528dfdf3d7ecbb51cd743e31f7b94495",
      "bytes": 1168
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "03473155b8347954926311cf2e59b15fa004baff06562facd7e8f77efc89d749",
      "bytes": 622
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "9c21ff48fc185f407cbe50727105ddd6c55de5b2033194c112826fe8fc9375cf",
      "bytes": 631
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "c4f2709f6c3a4d30ff0ad5bfb7e039ceeb959407d5216c59a38bb24bd3fff14b",
      "bytes": 115818
    }
  ],
  "estimated_tokens": 11633
}
-->

# Durable State Update — Chapter 397

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 397. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 397. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 397,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 397,
    "continuity_sources": [397],
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
    "The black knight serves an unnamed lord whose commands bind him completely, commands ten Death Knights across five legions, and personally leads one legion's vanguard.",
    "The black knight recognizes the attacked city as a place connected to memories of a child, light, and an unknown hand, but does not know his own origin or why he was sent there.",
    "The black knight understands human speech and can use a single greatsword stroke to destroy incoming shells, magic, and arrows before killing three A-rank Hunters and twenty B-rank Hunters.",
    "The undead assault force includes tens of thousands of monsters, Death Knights, roughly two hundred Dullahans, Lycanthropes, Gargoyles, Wyverns, and large monsters used in disciplined formations devised by the black knight.",
    "The Arch Lich deliberately made its regional power appear weaker, withdrew its armies to lower human vigilance, intensified communications interference, and then launched a coordinated surprise attack across the fronts.",
    "Communications with every front have been severed or delayed by at least thirty minutes, making current battlefield reports unreliable.",
    "Jin is being teleported alone from the command center to the hospital rooftop, with Magic Johnson estimating only a ten-percent chance of survival.",
    "Magic Johnson can teleport Jin despite the interference, but doing so risks both their lives; he agreed after Jin proposed using the missile-teleportation method without him accompanying Jin.",
    "Lei Fei remains missing with his unit, and Wei Fenghu still wants Jin to bring him back if found.",
    "The Second Fiend assigned to the Qingcheng attack remains unaccounted for."
  ],
  "continuity_sources": [
    396,
    395
  ],
  "open_questions": [
    "What is the black knight's identity and origin, and what is the significance of the child and city in his recovered memories?",
    "Who is the lord served by the black knight, and what is the Arch Lich's larger objective?",
    "Will Jin survive the dangerous teleportation and reach the hospital rooftop?",
    "What happened to Lei Fei and the Hunters who disappeared with him?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?"
  ],
  "safe_through": 396,
  "temporary_decisions": [
    "Render 파이 첸 as Faye Chen and 매직 존슨 as Magic Johnson.",
    "Render 전하 as His Highness for Prince Felix, including Jin's sarcastic use of the title.",
    "Preserve Magic Johnson's casual, flirtatious banter and Jin's dry, blunt resistance.",
    "Preserve Jin's profane and irreverent humor when he challenges authority figures.",
    "Render Death Knight as the capitalized Monster type and black knight as its lower-case leader title."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 무인     | **martial artist**                               | Default term                                          |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 일격     | **One Strike**                         |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 귀가      | **your family**                                                 |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 명장 | **Master Artisan** | Master craftsman capable of handling Ten-Thousand-Year Cold Iron |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 라이칸스로프 | **Lycanthrope** | B-rank Gate monster species. |
| 오크 | **Orc** | Monster species. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 인민해방군 | **People's Liberation Army** | Chinese military deployed to seal off the catastrophe area. |
| 듀라한 | **Dullahan** | Headless undead monster form taken by Yao Wei. |
| 데스나이트 | **Death Knight** | Undead commander type serving under the Black Knight. |
| 공안무력부 | **Public Security Armed Forces Department** | Chinese security organization ordered to assemble during the attack. |
| 악사르 | **Aksar** | Demon Realm word spoken by the Black Knight. |
| 가로쉬 | **Garosh** | Demon Realm word spoken by the Black Knight. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 394
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, and a Supreme Peak master who has manifested Force and crossed the wall into true mastery.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother; Jeok Cheongang is his Master; Cheongpung is his trusted companion and only true martial rival; his mother and sister Hayeon are among those he protects.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 394
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 396
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Team Leader in the Public Security Armed Forces Department who mediates between Jin and Shao Shen's enraged subordinates.
- **Personality:** Practical, emotionally aware, and attentive to the political consequences of violent decisions.
- **Voice:** Low, calm, and pragmatic, framing emotional choices through their consequences.
- **Relationships:** He supports Jin's intervention and works with Shao Shen's regiment during the aftermath of the massacre.

## Korean source

```text
＃397화



최 팀장, 아니 최민우는 생각했다.

‘어떻게 해야 할까.’

가파르게 두방망이질 치는 심장과 달리, 그의 머릿속은 차갑게 식어 있었다.

전투가 시작된 지 불과 30분. 급하게 구축한 방어진은 전투 개시와 동시에 허물어졌고, 그 틈새를 파고든 최상위 몬스터들이 무인지경(無人之境)으로 날뛰기 시작하자 그대로 찢겨 나갔다.

바로 지금처럼.

콰직!

날카로운 송곳니가 인간의 목을 거칠게 물어뜯었다.

바람 빠지는 소리와 함께 절명한 헌터를 내던진 라이칸스로프(Lycanthrope)가 포효했다.

- 아우우우우!

그리고 그것이 라이칸스로프의 유언이 되었다.

쉭, 서걱!

잿빛 털이 피로 물들고, 신형이 기울어진다. 군더더기 없는 일격으로 놈의 목을 날려 보낸 최민우가 숨 쉴 틈도 없이 허리를 젖혔다.

후우우웅! 퍼걱!

불과 한 뼘 차이.

불길한 마력이 넘실거리는 도끼날이 최민우를 스쳐 지나가 근처에 있던 오크 두 마리의 머리통을 박살 냈다.

목 없는 기사, 듀라한(Dullahan)은 동족을 죽였음에도 한 치의 거리낌 없이 눈앞의 인간을 향해 공격을 퍼부었다.

쐐애애애액! 서거걱!

- 크륵!

“커헉!”

거대한 할버드가 종횡으로 휘둘러지자 간격에 들어와 있던 인간과 몬스터의 신형이 조각난다.

듀라한은 동급의 헌터 셋이 있어야 안전하게 처리할 수 있다는 A급 몬스터.

하지만 미끄러지듯 공격을 피해 낸 최민우는 망설임 없이 검을 뻗었다.

‘지금!’

짧게 내뱉는 호흡. 그리고 섬광과도 같은 일격.

푸푹!

세 가지의 마법이 부여되고 명장이 벼려 낸 검날이 듀라한의 어깻죽지를 꿰뚫었다.

이미 한번 죽어 언데드가 된 탓에 고통을 느끼지는 못할지라도 그 육신은 인간의 것.

오른팔의 근육과 힘줄이 잘려 나가자 힘을 잃은 할버드가 땅에 처박혔다. 최민우는 그 순간을 놓치지 않았다.

촤아아아악!

듀라한의 허리를 양단하는 새하얀 오러(Aura). 죽은 지 얼마 되지 않은 놈인지, 허물어지는 듀라한의 몸뚱어리에서 뿜어져 나온 썩은 핏물이 얼굴을 적셨다.

그러나 코끝을 찌르는 엄청난 악취에도 그는 눈썹 하나 까딱하지 않았다.

지금의 최민우는 전장에서의 긴장감과 냉철한 이성, 미약한 흥분에 휩싸여 있었다.

‘열 마리째.’

오늘 최민우가 홀로 처치한 A급 몬스터의 숫자다. 그 이하 등급의 몬스터까지 합치면 족히 오십은 넘으리라.

‘내가 이 정도였나?’

그 질문에 냉정하게 대답한다면, 답은 No였다.

아크 리치의 영향 때문인지 중국에서 맞닥트린 몬스터는 조금 더 강했고, 훨씬 더 흉폭했다.

그럼에도 최민우가 이런 난전(亂戰)에서 뛰어난 활약을 펼칠 수 있었던 것은 두 가지 행운이 따랐기 때문이었다.

첫 번째.

‘진가심법.’

진태경에게 직접 사사한 마나 연공법.

최민우는 가문 대대로 내려온 가보라고 주장하는 진태경의 말에는 의구심을 품었지만, 이것이 훌륭한 비전이라는 데에는 아무런 이견이 없었다.

그가 익힌 진가심법은 기운을 안정적으로 제어하는 동시에 힘의 배분에 큰 도움이 되었고, 사사하는 과정에서 얻은 막대한 마나는 쉽게 지치지 않는 활력을 얻게 해 주었다.

그리고 두 번째 행운은…….

- 구워어어어!

쾅!

광포한 기세로 휘둘려진 철근이 시멘트 도로를 박살 냈다.

오우거의 두꺼운 팔을 밟으며 솟구친 최민우가 힘을 실어 검을 내리꽂았다.

푸욱!

오러가 실린 검날이 오우거의 정수리를 두부처럼 가르며 파고든다.

쿠쿵.

육중한 소리와 함께 무릎을 꿇는 4m의 거체. 숨이 끊긴 놈의 어깨를 밟고 선 최민우의 시선이 빠르게 주위를 훑었다.

‘없다.’

곳곳에서 비명과 죽음이 흘러넘치는 아비규환(阿鼻叫喚).

그러나 역시 보이지 않는다. 전투 시작과 동시에 믿기지 않을 만큼의 힘을 보여 준 그 괴물, 몬스터 군단의 사령관이며 데스나이트들의 우두머리가.

‘도대체 어디에 있는 거지?’

최민우는 똑똑히 기억하고 있었다. 단 한 번의 일격으로 수십의 헌터를 쓸어 버리던 검은 기사의 모습을.

만약 놈이 작정하고 나섰다면, 인간들은 삼십 분도 채 버티지 못하고 전멸했을지도 모른다.

하지만 어째서인지 검은 기사는 그 후로 모습을 나타내지 않았다.

자신이 나설 만큼 대단한 싸움이 아니라는 몬스터의 오만일까?

도무지 영문을 알 수 없는 일이었지만, 그건 최민우에게 주어진 두 번째 행운인 동시에 마지막 판단을 내릴 기회였다.

‘후퇴해야 해.’

이미 시가전(市街戰)은 의미를 잃었다. 일만을 헤아리는 몬스터 군단은 이미 개미 떼처럼 도시를 뒤덮었고 그중에는 백여 마리의 A급 몬스터가 포함되어 있다.

숫자에서도, 전력에서도 상대가 되지 않는 싸움.

이미 최전선을 지키던 천 명의 공안 무력부 헌터 중 절반에 가까운 숫자가 죽고 다쳤으며, 빌어먹을 인민해방군은 몬스터가 다가오기도 전에 태반 이상이 무기를 버리고 도망쳤다.

이미 고철 덩어리가 되어 버린 기갑 부대와 비행 몬스터의 제물이 되어 가고 있는 공군 전력은 덤이다.

투두두두두, 콰아앙!

중심을 잃고 추락한 최신예 전투 헬기가 화염과 함께 폭발했다. 튕겨 나간 파편에 휩쓸린 십여 명의 군인들은 비명도 지르지 못하고 절명했다.

끔찍한 광경이었지만 고통 없는 죽음이라는 면에서 보자면 그들은 행운아다.

뒤이어 몬스터 무리는 모두를 닥치는 대로 찢어발기기 시작했으니까.

- 크아아아아앙!

후웅, 뻑!

수 톤의 힘이 실린 샤벨 타이거의 앞발에 사지가 으스러지고, 머리통이 터져 나간다.

인민해방군 소속의 군인들은 헌터만큼 빠르지도 않았고, 그들이 들고 있는 소총은 몬스터들에겐 새총이나 다름없었다.

눈앞에서 벌어지는 무자비한 학살극에 최민우는 이를 악물었다.

‘정신 차려라. 저들을 모두 구할 수는 없어.’

위선자처럼 대를 위한 소의 희생을 입에 담지는 않았다. 다만 그는 냉철하게 상황을 직시했고, 이 무대의 악역이 될 준비를 끝마쳤다.

‘그가 와 줬다면 우린 놈들을 막아낼 수 있었을까.’

문득 진태경에 관한 생각이 들었지만 부질없는 미련일 뿐이다.

통신 장교를 닦달해 미친 듯이 긴급 신호를 보냈음에도 답이 없다.

계획적인 기습에 철저한 통신 방해까지.

지금으로서는 그저 바다에 띄운 수많은 유리병 중 하나가 그에게 닿기를 바랄 뿐이었다.

푸푹!

달려드는 미노타우로스의 가슴에 검을 박아넣은 최민우가 외쳤다.

“샤오 쉔!”

마나가 실린 외침이 비명과 굉음 사이를 뚫고 한 사람의 귓가에 닿았다.

상처와 핏물을 뒤집어쓴 채 끊임없이 밀려드는 몬스터들을 막아내던 샤오 쉔이 기합처럼 외쳤다.

「말씀하십시오!」

“공안무력부를 물리세요. 당장 후퇴해야 합니다!”

「예? 하지만 지금 후퇴하면…….」

곧 저 어린 헌터의 입에서 무슨 말이 나올지, 최민우는 이미 짐작하고 있었다.

가장 많은 사상자가 발생하는 것은 바로 후퇴 후 추격전에서다.

특히나 지금 같은 상황에서 마지막 방파제 역할을 하고 있던 헌터들이 물러난다면 인민해방군은 몬스터 군단의 손아귀에 떨어질 것이다.

“포위당하면 전부 끝장입니다. 알고 있습니까? 지금이라도 살아남은 헌터들과 후방 부대를 이끌고 도시에서 빠져나가야 합니다!”

「……최 선생님.」

“압니다. 무슨 생각인지. 하지만 우리에겐 남은 방법밖에 없습니다.”

「……!」

샤오 쉔은 자신도 모르게 눈을 질끈 감았다.

그도 지금 상황을 모르지 않았다. 아니, 누구보다 잘 아는 사람 중에 하나였다.

시작과 동시에 전황은 급격히 기울었고 인간들은 임시 사령부로 삼은 병원까지 밀려났다. 놈들의 포위망이 완전히 갖춰진다면…….

‘전멸.’

고민은 길었지만, 순간은 짧았다.

눈을 뜬 샤오 쉔은 쏟아지는 공격을 받아치며 있는 힘껏 외쳤다.

「후퇴! 공안무력부 전원, 현 시간부로 즉각 후퇴하라! 북문(北門)이 비어 있다!」

전시 상황에서 샤오 쉔과 같은 지휘관의 명령은 절대적이다.

랴오 상장을 포함한 군 수뇌부가 코빼기도 비추지 않았을 경우에는 더더욱 그렇다.

‘됐어.’

군인이라면 몰라도 헌터라면 생존 확률이 대폭 올라간다. 샤오 쉔이 바른 판단을 내린다면 저 중 상당수가 포위망을 뚫고 살아남을 수도 있을 것이다.

‘그래, 이걸로 된 거다.’

최민우는 마음이 가벼워지는 것을 느끼며 신형을 날렸다.

아직 몬스터가 막지 못한 북쪽이 아닌, 몬스터들에게 도륙당하고 있는 인민해방군을 향해서.

‘자살하러 가는 기분이군.’

자신은 왜 이런 선택을 한 걸까. 알다가도 모를 일이었다.

그래도…… 죽으러 가는 것치고는 기분이 썩 괜찮았다.

어느새 몰려온 먹구름 때문인지 바람도 서늘하고, 등 뒤에는 외롭지 않게 죽어 줄 길동무도 있었으니까.

최민우는 문득 입술을 뗐다.

“왜 후퇴하지 않았습니까?”

북문으로 향했어야 할 샤오 쉔이 희미한 웃음을 지어 보였다.

「최 선생님은요?」

“……제가 먼저 물었습니다.”

「그럼 먼저 대답해 드려야겠군요. 공안무력부!」

연대장의 부름에, 뒤를 따르던 삼백여 명의 헌터들이 우렁찬 외침을 토해 냈다.

「몬스터를 처치하고, 모든 위협으로부터 인민을 지키기 위함입니다!」

「이것이 우리가 후퇴하지 않는 이유입니다. 쓰촨성 공안무력부 1연대장 샤오 쉔 이하 325명, 인민을 지키기 위해 왔습니다!」

샤오 쉔의 나직한 목소리가 이어졌다.

「이제 최 선생님이 답하실 차례입니다.」

가까워지는 수천 마리의 몬스터를 말없이 바라보던 최민우가 불쑥 한마디를 내뱉었다.

“시부럴 거. 많이도 모였네.”

「……!」

“아마 그 사람은 이렇게 말했을 겁니다. 그리고 누구보다 치열하게 싸우고, 결국 승리했겠죠.”

맞다. 그는 늘 그랬다.

어떤 상황에서도 물러서는 법이 없었고 포기한 적도 없었다. 그 모습을 가장 오래, 그리고 가까이서 지켜본 최민우는 알고 있었다.

그 사람, 진태경은 새로운 시대의 영웅이며 자신은 결코 그처럼 기적을 일으킬 수 없다는 것을. 다만…….

“쪽팔리잖습니까.”

「예?」

“진태경 씨는 직급상으로 제 부하 직원이거든요. 이럴 때일수록 상사가 솔선수범해야지요.”

최민우는 샤오 쉔이 당황할 만큼 크게 소리 내어 웃었다.

마음은 민들레 홀씨처럼 홀가분했고, 적들을 향해 쏘아지는 전신에는 지금껏 느낄 수 없었던 알 수 없는 힘이 흘러넘쳤다.

‘진태경 씨. 나중에 봅시다.’

오늘 내가 살아난다면 가급적 빨리. 죽는다면 가급적 늦게.

그렇게 만나기로 합시다.

츠츠츠츠.

그 어느 때보다 선명하고 찬란한 오러를 머금은 검신이 적들을 향한다.

귀가 먹먹해지는 함성과 투지를 내뿜는 삼백여 명의 결사대가 그 뒤를 쫓아 화살처럼 쏘아졌다.

와아아아아아!

수천의 몬스터를 이끌며 인민해방군을 학살하던 데스나이트 두 기가 해골마에 올라 초라한 인간의 군세를 굽어보았다.

- 악사르. 가로쉬.

잠시 후, 검은 물결은 새하얀 조약돌을 집어삼켰다.

이미 결말이 정해져 있지만 어느 때보다 격렬했던 전투의 끝에, 처음부터 마지막까지 빛을 잃지 않았던 누군가의 검이 있었다.



* * *



자신들을 응시하는 검은 기사를 향해, 두 기의 데스나이트는 한쪽 무릎을 꿇었다.

- 전투에서.

- 승리를 거두었습니다.

- 오늘 이 영광을.

- 로드께 바칩니다.

고저 없이 뚝뚝 끊어지는 목소리. 승리 소식에도 검은 기사는 감흥 없이 고개를 끄덕였다.

예상대로였다. 인간들은 그의 강대한 군단을 막을 수 없었고, 일거에 무너져 내렸다.

그러나 모든 것이 검은 기사의 뜻대로 흘러갔느냐 묻는다면, 대답은 ‘아니’었다.

‘그때 그 인간들.’

개전과 동시에 도시를 돌파하고 인간들을 후퇴시킨 검은 기사는 마음 내키는 대로 말머리를 돌렸다.

그리고 어째서인지 익숙한 전날의 장소에서, 자그마한 무언가를 발견했다.

‘인간? 아니다. 인간이 아니라 아이다. 그리고 이건 신발.’

차례대로 떠오르는 기억과 단어들.

검은 기사의 생각대로 그건 아이의 신발이었다. 혼란한 와중에 흘린 것도 모른 채 남겨진 유아용 신발.

한없이 작은 흙투성이 신발을 보고 있노라면 왠지 모르게 익숙하고 가슴이 아팠다.

‘음? 가슴이 아프다?’

이 무슨 생소한 표현인가.

검은 기사는 처음부터 아픔을 느끼지 못하는 몸이었다. 주인은 그를 직접 탄생시키고 강력한 축복을 내려 주었다. 당연히 지치지도 않고, 고통도 느끼지 않는다.

무엇보다, 지금은 이런 하찮은 것에 휘둘릴 때가 아니었다.

- 로드.

- 무슨 문제라도.

왜 그랬는지는 모르겠다.

검은 기사는 손에 쥐고 있던 신발을 갑주 틈새 사이에 끼워 넣고는 화제를 돌렸다.

- 아니다. 그보다는 살아서 도망친 인간들이 꽤 되더군.

- 죄송합니다.

- 저희의 불찰입니다.

- 이유가 있을 터.

데스나이트들이 고개를 깊이 숙였다.

- 인간들의 발악이.

- 생각 이상으로 거셌습니다.

- 그 대신.

- 약간의 소득이 있었습니다.

마치 그 말을 기다렸다는 듯, 빽빽하게 군집해 있던 몬스터들이 좌우로 갈라지며 길을 비켰다.

조심스럽게 다가온 트롤 한 마리가 양어깨에 짊어지고 있던 것을 내려놓고 물러났다.

‘약간의 소득’을 바라보는 검은 기사의 안광이 일렁였다.

- 인간들이로군.

- 그렇습니다.

동시에 대답한 두 충복이 말을 이었다.

- 직접 영혼을 거두시어.

- 로드의 종으로 삼으시옵소서.

- 그리하면 로드께서는.

- 더욱더 강대해지실 것입니다.

맞는 말이다. 저 두 인간은 풍부하면서도 탐스러운 영혼을 가졌다.

직접 거두어 수하로 삼는다면 더욱 뛰어난 전사로 거듭날 것이고, 일군의 사령관을 맡겨봄 직하다.

하지만…….

‘왜지?’

검은 기사는 머뭇거리는 스스로를 발견했다.

이건 당연히 해야 할 일이다. 뛰어난 수하를 얻으면 군단은 강성해지고, 그것은 곧 그가 모시는 죽음의 왕에 대한 충성과 헌신을 의미하니까.

그런데 어찌하여 자신은 망설이고 있는가.

‘무엇이 나를 망설이게 하는가.’

평소였다면 석연찮음을 느끼며 물러났을 것이다. 그러나 검은 기사는 근래 들어 지금 같은 혼란을 너무나도 많이 겪었다.

그가 억지로 손을 뻗은 것은 스스로에 대한 반발심일지도 몰랐다.

- 너희의 뜻을, 받아들이마.

그리고 검은 기사의 손길이 두 인간의 영혼을 거두려던 그 순간.

“곰곰이 생각해 봤는데.”

허공에서 울려 퍼진 목소리에 검은 기사는 고개를 들었다.

반쯤 불타고 무너진 병원의 옥상 위, 누군가가 먹구름 사이로 비친 햇빛을 등지고 서 있었다.

“10% 이거, 의외로 높은 확률이란 말이지. 음. 내가 여자친구를 사귈 확률보다는 확실히 높아.”

검은 기사의 안광이 가늘어졌다. 전날, 멀리에서 느껴 본 적 있는 기운이다.

드디어 맞닥트린, 거대한 열기의 소유자.

- 넌. 누구지?

“나?”

스윽. 탁.

순식간이었다. 까마득한 높이에서 빠르게, 그러나 잎사귀처럼 가볍게 착지한 젊은 인간이 손가락으로 스스로를 가리키며 웃는다.

“나야 더럽게 운 좋은 새끼지.”

다음 순간, 검은 기사는 똑똑히 보았다.

자신을 향해 움직이는 인간의 손가락을. 동시에 모든 감정이 사라진 그의 얼굴을.

“너는, 뭐…….”

망자도 몸서리칠 만큼 차가운 목소리가 이어졌다.

“더럽게 운 나쁜 새끼고.”
```

## Final English reading copy

```markdown
# Chapter 397

Team Leader Choi—or rather, Choi Minwoo—thought,

*What should I do?*

Unlike his violently pounding heart, his mind was ice-cold.

Only thirty minutes had passed since the battle began. The hastily constructed defensive line had collapsed the moment the fighting started, and when the highest-grade monsters slipped through the gaps and began rampaging as if no one stood in their way, it had been torn apart completely.

Just like now.

Crunch!

Sharp fangs savagely bit into a human throat.

The Lycanthrope threw aside the Hunter it had killed with a wheezing exhalation and let out a roar.

—Awooooooooo!

And those became the Lycanthrope’s final words.

Whoosh. Slash!

Gray fur was dyed red, and its body tilted. Choi Minwoo decapitated it with a clean, waste-free strike, then bent backward without even a moment to catch his breath.

Whoooooom! Crack!

It had passed within a handspan.

An ax blade rippling with ominous magic grazed Choi Minwoo and smashed the heads of two Orcs nearby.

The headless knight, a Dullahan, attacked the human in front of it without the slightest hesitation, despite having killed one of its own kind.

Swoooooosh! Slash!

—Krrk!

“Guh!”

As the enormous halberd swept back and forth, the bodies of humans and monsters caught within its range were torn apart.

A Dullahan was an A-rank monster that required three Hunters of the same level to deal with safely.

But Choi Minwoo slipped past its attack like water and thrust out his sword without hesitation.

*Now!*

A short exhalation.

Then a strike as swift as a flash of light.

Thud!

The blade, enchanted with three different spells and forged by a Master Artisan, pierced through the Dullahan’s shoulder.

It had already died once and become undead, so it might not have felt pain. But its body was still human.

When the muscles and tendons of its right arm were severed, the halberd lost its strength and slammed into the ground. Choi Minwoo did not miss the opening.

Shhhhhk!

A blade of white aura cleaved the Dullahan in half at the waist. It must have died only recently, because rotten blood burst from its collapsing body and splattered across Choi Minwoo’s face.

But even in the face of the terrible stench stabbing at his nose, he did not so much as twitch an eyebrow.

Choi Minwoo was consumed by the tension of the battlefield, his cold reason, and a faint exhilaration.

*That makes ten.*

The number of A-rank monsters Choi Minwoo had defeated alone today. Including the monsters of lower grades, the number must have easily exceeded fifty.

*Was I always this strong?*

If he answered that question honestly, the answer was no.

Perhaps because of the Arch Lich’s influence, the monsters he had encountered in China were slightly stronger and far more ferocious.

Even so, Choi Minwoo had been able to perform so well in this chaotic battle because he had been blessed with two strokes of luck.

The first was—

*The Jin Family’s Cultivation Technique.*

The mana cultivation method he had learned directly from Jin Taekyung.

Choi Minwoo had been suspicious of Jin Taekyung’s claim that it was a family heirloom passed down through the generations. But he had no disagreement whatsoever that it was an outstanding secret technique.

The Jin Family’s Cultivation Technique he had learned allowed him to control his energy steadily while greatly improving his distribution of strength. The immense mana he had gained during his training had also given him stamina that let him fight without tiring easily.

And his second stroke of luck was—

—Gwoooooar!

Boom!

A rebar swung with berserk force smashed through the concrete road.

Choi Minwoo sprang upward, stepping on the ogre’s thick arm, and brought his sword down with all his strength.

Thrust!

The aura-infused blade split through the ogre’s crown as easily as tofu.

Thud.

The four-meter-tall giant dropped to its knees with a heavy crash. Choi Minwoo stood atop the shoulder of the dead creature and swept his gaze rapidly across his surroundings.

*He’s not here.*

A hellish scene overflowed with screams and death on every side.

But the monster was nowhere to be seen. The monster who had displayed unbelievable power the moment the battle began—the commander of the monster army and leader of the Death Knights.

*Where the hell is he?*

Choi Minwoo remembered the black knight clearly. With a single strike, it had swept aside dozens of Hunters.

If the creature had truly decided to join the battle, the humans might have been annihilated without lasting even thirty minutes.

But for some reason, the black knight had not appeared since then.

Was it the monster’s arrogance—the belief that this was not a battle worthy of its intervention?

Choi Minwoo could not understand it at all. But that was both the second stroke of luck he had been granted and his last chance to make a decision.

*We have to retreat.*

The urban battle had already lost all meaning. The monster army, numbering around ten thousand, had already covered the city like a swarm of ants. Among them were more than a hundred A-rank monsters.

They were outmatched in both numbers and strength.

Nearly half of the thousand Hunters from the Public Security Armed Forces Department who had been holding the front line were already dead or wounded. And more than half of the damned People’s Liberation Army had thrown down their weapons and fled before the monsters even approached.

The armored units, reduced to heaps of scrap metal, and the air force, becoming prey for the flying monsters, were simply more of the same.

Rat-a-tat-tat-tat-tat! Boom!

A state-of-the-art combat helicopter lost its balance and plunged from the sky, exploding in flames. Around a dozen soldiers caught in the flying debris died without even having time to scream.

It was a horrifying sight. But in terms of dying without pain, they were the lucky ones.

The monster horde began tearing everyone apart indiscriminately.

—Kraaaaaaang!

Whoom! Crack!

The foreleg of a Saber Tiger, carrying several tons of force, crushed a soldier’s limbs and burst his head.

The soldiers of the People’s Liberation Army were not as fast as Hunters, and the rifles they carried were no different from slingshots to the monsters.

Choi Minwoo clenched his teeth at the merciless slaughter unfolding before him.

*Pull yourself together. You can’t save all of them.*

He did not speak hypocritically of sacrificing the few for the sake of the many. He simply faced the situation with a cold eye and finished preparing himself to become the villain of this stage.

*Could we have stopped them if he had come?*

He suddenly thought of Jin Taekyung, but it was nothing more than useless regret.

Even after hounding the communications officer into sending emergency signals frantically, there had been no response.

A carefully planned ambush, combined with thorough communications interference.

For now, all he could do was hope that one of the countless glass bottles cast into the sea would somehow reach him.

Thud!

Choi Minwoo drove his sword into the chest of a charging Minotaur and shouted,

“Shao Shen!”

His mana-infused voice pierced through the screams and thunderous crashes and reached one person’s ears.

Shao Shen, covered in wounds and blood as he fought back the endless stream of monsters, shouted in response like a battle cry.

「Speak!」

“Withdraw the Public Security Armed Forces Department. We have to retreat now!”

「What? But if we retreat now…」

Choi Minwoo already knew what the young Hunter was about to say.

The greatest number of casualties occurred during the pursuit after a retreat.

Especially in a situation like this, if the Hunters who had been serving as the last barrier withdrew, the People’s Liberation Army would fall into the monster army’s grasp.

“If we get surrounded, it’s all over. Do you understand? Even now, you need to lead the surviving Hunters and the rear units out of the city!”

「……Mr. Choi.」

“I know what you’re thinking. But we have no other choice.”

「……!」

Shao Shen squeezed his eyes shut without realizing it.

He knew the situation. No—he was one of the people who understood it better than anyone.

The battle had turned sharply against them from the very beginning, and the humans had been driven all the way back to the hospital they were using as a temporary command center. If the monsters completed their encirclement—

*Annihilation.*

He had thought for a long time, but the moment itself was brief.

Shao Shen opened his eyes and shouted with all his strength while deflecting the attacks raining down on him.

「Retreat! All Public Security Armed Forces Department personnel, withdraw immediately! The North Gate is open!」

During wartime, the command of a commander like Shao Shen was absolute.

All the more so when the military leadership, including Senior General Liao, had not even shown their faces.

*Good.*

The soldiers might not have much hope, but the Hunters’ odds of survival would rise dramatically. If Shao Shen made the right calls, a considerable number of them might be able to break through the encirclement and survive.

*Yes. This is enough.*

Feeling his heart grow lighter, Choi Minwoo threw himself forward.

Not toward the North Gate, which the monsters had yet to block, but toward the People’s Liberation Army being slaughtered by the monsters.

*It feels like I’m going to kill myself.*

Why had he made this choice? Even he could not understand it.

Still…

For something that amounted to going to his death, he felt surprisingly good.

Perhaps because dark clouds had gathered overhead, the wind was cool. And behind him, he had companions who would die alongside him, so he would not have to die alone.

Choi Minwoo suddenly parted his lips.

“Why didn’t you retreat?”

Shao Shen, who should have been heading toward the North Gate, gave him a faint smile.

「What about you, Mr. Choi?」

“……I asked first.”

「Then I suppose I should answer first. Public Security Armed Forces Department!」

At the regimental commander’s call, the roughly three hundred Hunters following behind him released a thunderous shout.

「To eliminate monsters and protect the people from every threat!」

「This is why we do not retreat. The 325 members of the Sichuan Province Public Security Armed Forces Department’s 1st Regiment, led by Regimental Commander Shao Shen, have come to protect the people!」

Shao Shen’s quiet voice followed.

「Now it is your turn to answer, Mr. Choi.」

Choi Minwoo silently gazed at the thousands of monsters drawing closer, then suddenly muttered,

“Fuck. Quite a crowd.”

「……!」

“That man probably would have said something like that. And he would have fought harder than anyone else, then won in the end.”

It was true. He had always been that way.

He had never retreated from any situation and had never given up. Choi Minwoo, who had watched him from closer and for longer than anyone else, knew that.

That man, Jin Taekyung, was a hero of the new age, while Choi Minwoo could never create miracles the way he did.

But still—

“It’s embarrassing.”

「What?」

“Jin Taekyung is technically my subordinate, you see. This is when a superior should lead by example.”

Choi Minwoo burst into laughter, loudly enough to leave Shao Shen bewildered.

His heart felt as light as a dandelion seed, and an indescribable power surged through his body as he launched himself toward the enemies.

*Mr. Jin. I’ll see you later.*

If I survive today, as soon as possible.

If I die, as late as possible.

Let’s meet then.

Hissssss.

The blade of his sword, filled with aura brighter and more radiant than ever, pointed toward the enemies.

The roughly three hundred-strong death squad, roaring loud enough to deafen the ears and overflowing with fighting spirit, shot forward behind him like arrows.

“Waaaaaaaah!”

Two Death Knights who had been leading thousands of monsters and slaughtering the People’s Liberation Army looked down from their skeletal warhorses at the pitiful human force.

—Aksar. Garosh.

A moment later, the black wave swallowed the white pebbles.

The battle’s conclusion had already been decided. Yet at the end of the fiercest battle of all, there was a sword belonging to someone whose light had never faded from beginning to end.

* * *

The two Death Knights dropped to one knee before the black knight watching them.

—In the battle—

—we achieved victory.

—Today, this glory—

—we offer to our Lord.

Their voices were clipped and devoid of intonation. Even at the news of victory, the black knight merely nodded without interest.

It had gone as expected. The humans had been unable to stop his mighty army and had collapsed all at once.

But if someone asked whether everything had unfolded according to the black knight’s wishes, the answer would have been no.

*Those humans from back then.*

After breaking through the city and forcing the humans to retreat at the start of the battle, the black knight had casually turned his warhorse around.

And at the previous day’s location—a place that felt strangely familiar—he had found something small.

*Human? No. Not human. A child. And this is a shoe.*

Memories and words surfaced one after another.

As the black knight had thought, it was a child’s shoe. A tiny infant’s shoe left behind during the chaos, without anyone realizing it had been dropped.

Looking at the unbelievably small, dirt-covered shoe, he felt that it was strangely familiar. His chest hurt.

*Hm? My chest hurts?*

What an unfamiliar expression.

The black knight’s body had been incapable of feeling pain from the beginning. His master had created him personally and given him a powerful blessing. Naturally, he did not tire, nor did he feel pain.

More importantly, this was no time to be swayed by something so trivial.

—Lord.

—Is something wrong?

He did not know why he had done it.

The black knight tucked the shoe he held into a gap between the plates of his armor and changed the subject.

—No. Rather, quite a few humans managed to escape alive.

—We apologize.

—It was our failure.

—There must be a reason.

The Death Knights bowed their heads deeply.

—The humans’ resistance—

—was fiercer than expected.

—In exchange—

—we gained a small prize.

As if they had been waiting for those words, the densely packed monsters parted left and right, opening a path.

A Troll cautiously approached, lowered what it had been carrying across its shoulders, and stepped back.

The black knight’s eyes shimmered as he looked at the “small prize.”

—They are humans.

—Yes.

The two loyal retainers answered at the same time, then continued.

—Personally reap their souls—

—and make them servants of our Lord.

—If you do so, Lord—

—you will grow even mightier.

They were right. Those two humans possessed rich and desirable souls.

If he personally reaped them and made them his subordinates, they would be reborn as even more outstanding warriors. They might even be entrusted with command over an entire force.

But—

*Why?*

The black knight realized that he was hesitating.

This was something he obviously had to do. Gaining powerful subordinates would strengthen the legion, which in turn meant loyalty and devotion to the King of Death whom he served.

So why was he hesitating?

*What is making me hesitate?*

Under normal circumstances, he would have withdrawn, feeling that something was wrong. But recently, the black knight had experienced this kind of confusion far too many times.

The fact that he had forced himself to reach out might have been an act of defiance against himself.

—I will accept your suggestion.

And the moment the black knight’s hand reached out to reap the souls of the two humans—

“I’ve been thinking about it carefully.”

A voice rang out through the air, and the black knight raised his head.

On the roof of the half-burned, half-collapsed hospital, someone stood with the sunlight shining through the dark clouds behind him.

“Ten percent is surprisingly high when you think about it. Hmm. It’s definitely higher than my chances of getting a girlfriend.”

The black knight’s eyes narrowed. It was the same energy he had sensed from afar the day before.

At last, he had come face-to-face with the owner of that immense heat.

—Who are you?

“Me?”

Swish. Tap.

It happened in an instant. A young human dropped rapidly from a dizzying height, yet landed as lightly as a leaf. Pointing at himself with one finger, he grinned.

“I’m a son of a bitch who’s disgustingly lucky.”

The next moment, the black knight saw it clearly.

The human’s finger moving toward him.

And the expression on the human’s face, from which every emotion had vanished.

“You’re, what…”

A voice cold enough to make even the dead shudder continued.

“You’re a son of a bitch who’s disgustingly unlucky.”
```
