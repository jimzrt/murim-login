<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0803.txt",
      "sha256": "53f45ed37a566bd90e32bedb28925b35b428c76e5482df7bc3cb4a9865c081c4",
      "bytes": 12527
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "212e6f87be75ae4eea118a7249c54728e98917f6cfcf76dd074752d2c308a779",
      "bytes": 1735
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b1691d3d994f985fb5b3ee235809bb9586ff0efb33a460fc8cb138a6b2b0e1f6",
      "bytes": 224592
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "fd1fa9a53a3b9baf5b6f49ecdbc60d91b737961d1b9d0761871c39b79c1e524f",
      "bytes": 553
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "9d858723b674ce6a91fb5fd16c3c8baeffdb3b04de648b2813f8e5a5acec980f",
      "bytes": 667
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "3c9e9c3949fac1cf9c5689f6bac43acd2cb0a47231cde424f5c0f11367018e4a",
      "bytes": 707
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8f35dc58e43912ac49e8f00d38d106f1430d346d27f8a4c09f50a87eb53641ab",
      "bytes": 247115
    }
  ],
  "estimated_tokens": 8744
}
-->

# Durable State Update — Chapter 803

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 803. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 803. Profile updates may replace only one
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
  "chapter": 803,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 803,
    "continuity_sources": [803],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and pursues Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "The Prophet directed Jin’s force to the Rub’ al Khali, where the magical-power concentration exceeds surveillance equipment’s capacity.",
    "The Desert Storm has begun: Jin’s nearly one-thousand-Hunter force faces a monster army of at least ten thousand led by four likely S-rank monsters.",
    "The Skeleton King’s undead scouts provide aerial reconnaissance; he has not identified The Prophet among the enemy leaders.",
    "Chuck Hagel’s force guards the rear, but part of its outside search party has been attacked by an unidentified non-monster enemy.",
    "The Prophet stopped J1’s transport vehicles and absorbed blood and pale mist from the dead; the nature and limits of this power remain unknown.",
    "Amir and Hamid lead a concealed group near a convoy of more than five hundred people and await The Prophet and the coming holy war."
  ],
  "continuity_sources": [
    801,
    802
  ],
  "open_questions": [
    "Which of the four apparent S-rank monsters is The Prophet, and what are The Prophet’s identity, abilities, and limits?",
    "What was the pale mist absorbed from the J1 victims?",
    "What is the identity and objective of the non-monster enemy that attacked Chuck Hagel’s search party?",
    "Where is Amir’s concealed group now, and what is its intended target?"
  ],
  "safe_through": 802,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Render 조센징 as “Chōsenjin,” identifying it as an ethnic slur."
  ],
  "version": 1
}
```

## Exact glossary matches

| 살성     | **Slaughter Saint**           | —              |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 초식     | **form**                                         | Numbered technique movement                           |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 몬스터     | **monster**           |
| 대격변     | **Great Cataclysm**   |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화룡신창 | **Fire Dragon Divine Spear** | Taekyung's spear technique, at the seventh stage in this chapter. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 천격 | **Heavenly Strike** | A Fire Dragon Divine Spear form used by Taekyung against Hwangbo Eom. |
| 유령환살보 | **Ghost Illusory Slaughter Step** | Movement technique used by the Slaughter Saint. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 알라 | **Allah** | Deity invoked by the Middle Eastern terrorist groups' rhetoric. |
| 핫산 | **Hassan** | Subordinate addressed by the unidentified intruder. |
| 인벤토리 | **Inventory** | System storage summoned by Jin. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 신병이기 | **divine weapon** | Jin's description of White Flame. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 하미드 | **Hamid** | Amir’s subordinate, addressed by name. |
| 아미르 | **Amir** | Title used to address the group’s leader. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 하미드 | 아미르 | subordinate to leader | Amir | formal and deferential | Apologizes for speaking out of turn and addresses the leader as Amir. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 802
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 774
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 802
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a monster posing as the leader of the revived Hasasin, whose power includes stopping transport vehicles and absorbing blood and a pale mist from the dead.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

## Korean source

```text
＃803화



인간은 무한에 가까운 가능성을 지닌 존재다.

그들은 지구상의 어떤 생명체보다 뛰어난 사고력을 바탕으로 자신들만의 체계를 구축하여 문명을 발전시켜 왔다.

미개하기 그지없던 선사시대부터 현재에 이르기까지.

특히 지난 수천 년간 인간이 쌓아 올린 역사와 문물은 그야말로 눈부실 지경이었다.

발전, 발전, 또 발전.

인간은 끊임없이 새로운 무언가를 발견했고 그만큼 나아갔다.

창칼이 부딪치던 전장을 총성으로 메우고, 화려한 네온사인으로 물든 거리에 말의 울음소리 대신 자동차 경적이 울려 퍼질 때까지.

다섯 개의 바다와 여섯 개의 대륙을 넘어, 마침내 우주로 향할 때까지.



‘휴스턴, 이곳은 고요의 기지. 이글은 착륙했다(Houston, Tranquility Base here. The Eagle has landed).’



고대 신화 속 태양신의 이름을 딴 원대한 계획이 성공한 그날.

처음으로 달을 딛고 선 어느 인간이 ‘작은 발걸음이자 인류의 도약’이라 칭한 그 역사적인 순간을 어딘가에서 지켜보던 신은 무슨 생각을 했을까.

누구도 신의 뜻을 알 수는 없었지만, 압둘라 빈 압둘아지즈 알리라는 다소 긴 이름을 지닌 노인은 확신할 수 있었다.

신께서는 분노하셨을 것이다.

그렇지 않았다면 대격변이라는 이름의 대홍수를 일으키지 않았을 테니까.

위대한 선지자를 이 땅에 내려보내 저들을 벌하라 하신 것은, 당신을 대신하여 인간의 오만함을 치죄(治罪)하라는 뜻이 분명했다.

“너 역시 그리 생각하지 않느냐, 죄 많은 이교도여.”

“……!”

노인의 담담한 목소리에 중년인이 몸을 부르르 떨었다.

붉은 선혈을 흠뻑 뒤집어쓴 그의 주위에는, 조금 전까지만 하더라도 살아 숨 쉬던 수많은 부하들이 널브러져 있었다.

이제 중년인에게 남은 것은 아무것도 없었다.

손에 들린 한 자루의 검과, 아직도 투지를 잃지 않고 몸속에서 끓어오르는 마나를 제외한다면.

“죽음으로 속죄하거라. 먼저 떠난 저들처럼.”

“좆…… 까!”

비명과도 같은 외침과 함께, 온 힘을 끌어올린 중년인은 늙은 광신도를 향해 쇄도했다.

쐐애애액!

아마도 생애 마지막이 될 일격.

그 어느 때보다 쾌속하게 나아간 검에는 눈부신 오러가 담겨 있었고.

서걱!

불현듯 들이닥친 섬광은, 오러에 휩싸인 검과 주인을 동시에 갈랐다.

푸화악!

핏물이 분수처럼 솟구쳤다.

목이 날아간 시체가 허물어지듯 쓰러짐과 동시에 반짝이는 무언가가 노인의 발치 아래에 떨어졌다.

목걸이. 그것은 목걸이였다.

뜨겁게 달구어진 모래 사이에 파묻힌 십자가 목걸이를 물끄러미 바라보던 노인이 문득 입을 열었다.

“생존자는?”

“없습니다. 저 이교도가 마지막이었습니다.”

A급 헌터였던 중년인을 숨 쉬는 것처럼 자연스럽게 베어 버린 청년이 말을 이었다.

“아미르, 그리 멀지 않은 곳에 또 다른 이교도들이 있습니다. 절 보내 주신다면…….”

“이번에는 놈들의 본대까지 무전이 닿았을 거다. 지금까지는 손쉽게 처리했지만, 지금부터는 아니야.”

“이교도의 군세가 아무리 강하다 한들, 우리는 놈들을 쓰러트릴 수 있습니다!”

“핫산의 아들 하미드여, 네 말이 옳다. 그러나 선지자께서 하신 말씀을 잊었느냐?”

노인의 형형한 눈빛에, 하미드라 불린 청년은 자신도 모르게 몸을 움찔했다. 그리고 뒤늦게 그가 한 말의 의미를 깨닫고 눈을 크게 떴다.

“선지자께서 하신 말씀이라면, 설마?”

“그래, 드디어 때가 왔다. 선지자께서, 위대하신 알라께서 약속하신 때가 도래했다.”

“……!”

놀라움이 환희로. 환희에서 격동으로.

시시각각 변하는 청년의 얼굴을 보며 노인은 미소 지었다. 그리고 주위를 에워싼 신의 전사들을 굽어보며 뇌까렸다.

“인샬라. 선지자께서 약속의 땅으로 우리를 인도하신다!”

“인샬라!”

“알라 후 아크바르!”

한목소리로 외치는 거대한 외침과 함께, 수십 년의 세월 동안 사막 깊숙이 잠들어 있던 수많은 광신도들은 진격을 시작했다.

오랫동안 기다려 온 약속의 땅으로.

신의 은총이 충만한 그곳으로.

두두두두!

거대한 모래 구름이, 사막을 가로질렀다.



* * *



이 세상이 하나의 체스판이라면, 내 역할은 무엇일까.

그저 앞으로만 전진하는 폰?

폰보다 더 멀리 나아가는 나이트?

대각선을 따라 비스듬히 판을 누비는 비숍?

어쩌면 종횡으로 이동하는 룩이나, 비숍과 룩을 합친 힘을 지닌 퀸, 혹은 아이러니하게도 가장 중요하면서도 퀸보다는 약한 킹일 수도 있다.

사실 잘 모르겠다.

세계 헌터 연맹의 맹주가 된 지금도, 세상 사람들 모두가 나를 아는 이 상황에서도 내 정확한 위치가 어디쯤인지.

이 체스판에서 내가 어디서부터 어디까지 할 수 있을지.

하지만 한 가지만큼은 장담할 수 있다.

그 체스판의 이름이 세상이 아닌 전장(戰場)이라면, 나는 그곳을 지배할 수 있다고.

폰처럼 우직하게 전진하다가도 나이트가 되어 적들의 머리를 뛰어넘고, 비숍과 룩, 퀸처럼 사방을 종횡하며 모든 것을 집어삼킬 수 있다고.

바로 지금처럼.

파아아앙!

창날에 닿기도 전에 터져 나가는 살과 뼈. 상반신이 날아간 트롤의 몸뚱어리가 썩은 통나무처럼 쓰러지자, 등 뒤에서 누군가의 외침이 들려왔다.

“이런 빌어먹을! 그렇게 죽이면 언데드로 써먹기도 힘들다고 몇 번을 말하나!”

나는 대답 대신 몸을 비틀었다.

후웅, 쾅!

세 방향에서 동시에 날아온 플레일(Flail)이 서로를 향해 얽혀든다.

― 크워?

한 박자 늦게 상황을 깨달은 오우거들이 멍청한 표정으로 눈을 깜빡였다.

하지만 이미 백염의 창날은 놈들의 목줄기를 스쳐 지나간 뒤였다.

서걱!

거대한 몸뚱어리에서 떨어져 나온 세 개의 머리가 허공으로 솟구친다.

이미 생명이 빠져나간 오우거의 시체를 밟고 솟구친 나는, 빽빽하게 사방을 에워싼 몬스터들을 향해 내리꽂혔다.

화룡신창(火龍神槍) 이 초식.

천격(天格).

콰드드드드득!

피가 튀고 살이 갈라진다.

띠링. 띠링, 띠링.

쉴 새 없이 귓가로 전해지는 시스템 알림을 들으며, 나는 자욱하게 피어오른 먼지구름 사이로 뛰어들었다.

‘인벤토리 오픈.’

수납, 그리고 동시에 이루어진 소환.

팟.

손에 들린 백염이 허깨비처럼 사라지고, 그 대신 두 자루의 짧은 단검이 비어 있던 손아귀를 단단히 채운다.

지금 같은 초근접전 상황에서만큼은, 어떤 신병이기보다 빠르고 효율적인 무기.

그중에서도 내가 가까이서 지켜본 적 있는 누군가는, 이와 같은 한 자루의 비수로 살성(殺星)이라는 별호를 얻었다.

‘난 그걸 바로 옆에서 지켜봤고.’

짧은 순간, 나는 호흡을 가다듬었다.

터질 듯이 맥동하는 공력을 가라앉히고, 발끝은 가볍게. 어깨는 느슨하게.

살성의 조언을 떠올리며 수십 번이나 바로 앞에서 보았던 그의 움직임을 따라 했다.

그리고, 발걸음을 뗐다.

‘유령환살보(幽靈幻殺步).’

쉬릭.

언제나 강하게 부딪쳐 왔던 바람이 부드럽게 흩어진다.

마치 무중력 상태에서 허공을 부유하는 듯한 느낌.

물론 고작 이 정도로 살성의 독문 무공을 고스란히 따라 했다고는 말할 수 없었지만, 지금 당장 놈들을 상대하는 데에는 ‘고작 이 정도’만으로도 충분했다.

서걱, 서걱, 서걱!

살과 뼈를 베어 가른 뒤에야 들려오는 절삭음.

소리가 느린 것이 아니다.

바로 내가, 이 양손에 들린 단검이 소리를 밀어낼 만큼 빨랐다.

푸푸푸푹!

안개처럼 스며들어, 섬광처럼 찌르고 휘두르는 두 개의 단검에 수십여 마리가 피를 흩뿌리며 쓰러진다.

아니, 정확히는 쓰러짐과 동시에 다시 일어난다.

― 왕의 이름으로 명하노니, 부름에 답하라.

스아아아아.

귀가 아닌 머릿속에 울려 퍼지는 듯한 목소리와 함께, 스산한 한기(寒氣)가 전장을 휩쓸었다.

그것이 조금 전 쓰러졌고 지금 이 순간에도 쓰러져 가고 있는 몬스터들을 일으켜 세운다.

― 극. 그르륵.

느릿느릿한 울음소리.

눈동자 깊숙한 곳에서 섬뜩하게 빛나는 안광(眼光).

죽음의 끝자락에서 새로운 존재로 거듭난 언데드 군단은, 왕의 명령에 따라 사방에서 쉴 새 없이 몰려드는 몬스터들을 향해 일말의 망설임 없이 달려들었다.

― 크아아아아!

― 그. 어. 어. 어!

쿵. 콰아앙!

같으면서도 다른 몬스터의 괴성이 뒤얽히고, 세차게 휘두른 무기가 서로의 몸뚱어리를 후려친다.

그러나 살아 있기에 고통을 느낄 수밖에 없는 몬스터들과 달리, 언데드는 죽음과 함께 고통을 잊은 괴물들이었다.

― 그아아.

우적! 푸화악!

수적 열세? 그런 것 따위는 상관없었다.

사방에서 날아드는 무기에 팔다리가 날아가고, 가슴이 관통당해도 그것들은 마지막까지 움직였다.

스켈레톤 킹이 놈들에게 부여한 목표는 오직 하나.

그가 부여한 마력이 다하기 전에, 두 번째 죽음을 맞이하기 전에 또 다른 병사를 탄생시키는 것뿐이었으니까.

콰직!

― 끄아아아!

목줄기가 뜯겨 나간 몬스터가 울부짖는다.

이미 팔과 다리를 하나씩 잃은 언데드의 몸뚱어리가 분노한 괴물들에 의해 갈가리 찢겼지만, 아무래도 상관없었다.

그 덕분에 또다시 내가.

아니, 우리가 약간의 시간을 벌었으니까.

“발사!”

“파이어 월!”

“라이트닝 스피어!”

화아아악.

허공을 가로지르며 날아드는 무수한 벼락과 불길.

마치 바리케이트처럼 앞을 가로막은 거대한 수송 차량 뒤, 블랙 프라이데이 첫날 이마트처럼 물샐 틈 없이 몰려 있던 몬스터들은 갑작스럽게 쏟아진 공격을 고스란히 감당할 수밖에 없었다.

치직, 콰아아아!

― 크아아아아아!

― 커헉, 크르륵!

사방을 가득 메우며 울려 퍼지는 비명.

뇌전이 비늘과 살을 지지고, 그 틈새로 스며든 화염이 뼈와 내장을 불태운다.

심지어 지금껏 느껴본 적 없는 고통에 몸부림치던 수백 마리의 몬스터 중 상당수는 아군을 향해 무기를 휘두르기도 했다.

― 카우우우우!

본능 그 자체인 흉포함에 사로잡혀 서로를 향해 달려드는 괴물들.

그러나 나는 조금도 방심하지 않았다.

“대열 유지! 그 자리에서 한 발자국도 움직이지 마!”

공력을 실어 외친 명령에, 승기를 잡았다는 흥분과 전투의 열기에 고취되어 앞으로 전진하던 헌터들이 발걸음을 멈췄다.

전투는 흐름이고, 기세다.

그러나 기세를 타는 것도 때가 있다.

일만을 훌쩍 뛰어넘는 저 대병력 앞에서, 고작 천여 마리의 몬스터를 덜어 낸다 한들 이 전투에서 단숨에 승리할 수는 없다.

천천히. 침착하게.

피해를 최소화하면서도 승리를 가져와야 한다.

더군다나…….

‘아직, 놈이 보이지 않는다.’

지금까지도 모습을 드러내지 않은 그놈.

선지자.

거기에 더해 저 수많은 괴물들 속에서, 혹은 하늘 위 허공에서 때를 기다리고 있는 S급 몬스터들.

놈들을 쓰러트리지 않는 이상은 이 전투도, 전쟁도 끝나지 않는다.

‘이 싸움은…… 지금부터가 시작이다.’

그리고 내가 마음 깊숙이 뇌까린 그 순간.

쿵. 쿵. 쿠웅.

저 멀리에서부터 전해진 거대한 마력이, 사막을 떨어 울리기 시작했다.
```

## Final English reading copy

```markdown
# Chapter 803

Human beings possess possibilities close to infinite.

With their capacity for thought surpassing that of any other living thing on Earth, they built systems of their own and developed civilization.

From the utterly primitive prehistoric age to the present.

In particular, the history and culture humans had built over the past several thousand years were truly dazzling.

Progress, progress, and more progress.

Humans kept discovering new things, and moved forward with every one of them.

Until they filled battlefields where spears and swords once clashed with the sound of gunfire, and car horns rang through streets ablaze with neon signs instead of the whinnying of horses.

Until they crossed five seas and six continents, and finally ventured into space.

*“Houston, Tranquility Base here. The Eagle has landed.”*

On the day that grand plan, named after an ancient sun god, succeeded.

What had the god, watching from somewhere, thought at that historic moment when a human first set foot on the moon and called it “one small step, one giant leap for mankind”?

No one could know the will of God, but an old man with the rather long name of Abdullah bin Abdulaziz Ali could be certain.

God must have been enraged.

Otherwise, He wouldn’t have unleashed a great flood called the Great Cataclysm.

Sending the great Prophet down to this land and commanding him to punish them surely meant that he was to punish humanity’s arrogance on God’s behalf.

“Do you not think so as well, you sinful infidel?”

“……!”

At the old man’s calm voice, the middle-aged man trembled.

Drenched in crimson blood, he stood amid his many subordinates, who had been alive and breathing only moments ago and now lay strewn across the ground.

The middle-aged man had nothing left.

Nothing but the sword in his hand and the mana still boiling through his body, his fighting spirit undiminished.

“Repent through death. Like those who went before you.”

“Go… fuck yourself!”

With a scream, the middle-aged man drew on every ounce of his strength and charged at the old fanatic.

*Whoooosh!*

Perhaps the last strike of his life.

The sword flew faster than ever before, filled with blinding aura, and—

*Shhk!*

A flash came out of nowhere, cleaving both the aura-wreathed sword and its wielder in two.

*Splatter!*

Blood gushed like a fountain.

As the headless corpse crumpled to the ground, something glinting fell at the old man’s feet.

A necklace. It was a necklace.

The old man stared at the crucifix necklace half-buried in the hot sand, then suddenly spoke.

“Any survivors?”

“None. That infidel was the last.”

The young man who had cut down the middle-aged A-rank Hunter as casually as breathing continued,

“Amir, there are more infidels not far from here. If you let me go…”

“Their main force will have heard from them on the radio this time. We’ve dealt with them easily so far, but that ends now.”

“No matter how strong the infidels’ forces are, we can defeat them!”

“Hamid, son of Hassan, you’re right. But have you forgotten what the Prophet said?”

At the old man’s piercing gaze, the young man named Hamid flinched without meaning to. Then, realizing the meaning of his words a moment later, his eyes widened.

“If you mean what the Prophet said, then could it be…?”

“Yes. The time has finally come. The time promised by the Prophet, by almighty Allah, has arrived.”

“……!”

Amazement turned to joy. Joy to fervor.

Watching the young man’s expression change by the second, the old man smiled. Then he looked down at the warriors of God surrounding them and muttered,

“Inshallah. The Prophet will lead us to the promised land!”

“Inshallah!”

“Allah hu akbar!”

With their enormous voices rising as one, the many fanatics who had lain dormant deep in the desert for decades began their advance.

Toward the promised land they had awaited for so long.

Toward that place overflowing with God’s grace.

*Rumble, rumble, rumble!*

A vast cloud of sand swept across the desert.

* * *

If this world were a chessboard, what would my role be?

A pawn that can only move forward?

A knight that can leap farther than a pawn?

A bishop that traverses the board diagonally?

Maybe a rook that moves in straight lines, a queen with the combined power of a bishop and a rook, or, ironically, the king—both the most important piece and weaker than the queen.

Honestly, I didn’t know.

Even now, as the Alliance Leader of the World Hunter Federation, even with everyone in the world knowing who I was, I still didn’t know exactly where I stood.

Or how far I could go on this chessboard.

But there was one thing I could say for sure.

If that chessboard wasn’t called the world, but the battlefield, then I could dominate it.

I could keep pushing forward like a pawn, then become a knight and leap over the enemy’s heads; I could range across the board in every direction like a bishop, rook, or queen, and swallow everything whole.

Just like right now.

*Baaang!*

Flesh and bone burst apart before the spearhead even touched them. A Troll’s body, its upper half blown away, fell like a rotten log, and someone shouted behind me.

“Damn it! How many times do I have to tell you that if you kill them like that, they’re no use as undead!”

Instead of answering, I twisted my body.

*Whoom. Boom!*

Three flails flying in from different directions tangled together.

—Kwo?

The ogres blinked stupidly, realizing what had happened a beat too late.

But White Flame’s spearhead had already swept past their necks.

*Shhk!*

Three heads flew into the air, severed from their massive bodies.

I sprang off the corpse of an ogre whose life had already left it, then plunged down toward the monsters packed tightly around me.

Fire Dragon Divine Spear, Form Two.

Heavenly Strike.

*Krrrunch!*

Blood sprayed and flesh split.

Ding. Ding, ding.

As System alerts reached my ears without pause, I plunged through the thick cloud of dust.

*Open Inventory.*

Stowed away, then summoned in the same instant.

*Pop.*

White Flame vanished from my hand like an illusion, replaced by two short daggers that firmly filled my empty palms.

In a fight at this close range, they were faster and more efficient than any divine weapon.

Among those who had used weapons like these, there was someone I’d watched up close who had earned the epithet Slaughter Saint with a single dagger.

*I watched him from right beside him.*

For one brief moment, I steadied my breathing.

I calmed my internal energy, pounding as if it would burst, and kept my toes light and my shoulders loose.

Remembering the Slaughter Saint’s advice, I imitated the movements I’d seen him perform right in front of me dozens of times.

Then I took a step.

*Ghost Illusory Slaughter Step.*

*Swish.*

The wind, which had always slammed into me with force, scattered softly.

It felt as if I were floating through the air in zero gravity.

Of course, I couldn’t claim I’d perfectly copied the Slaughter Saint’s personal martial art just by doing this much. But for dealing with these bastards right now, this much was enough.

*Shhk, shhk, shhk!*

Only after flesh and bone had been cut through did the sound of slicing reach my ears.

It wasn’t that the sound was slow.

I was simply that fast—the daggers in my hands were moving fast enough to leave the sound behind.

*Thud, thud, thud!*

Seeping in like mist, then stabbing and slashing like flashes of light, the two daggers sent dozens of monsters crashing down in sprays of blood.

No—in truth, they fell and rose again at the very same moment.

—In the king’s name, I command you: answer the call.

*Whoooooosh.*

A voice that seemed to reverberate inside my head rather than my ears rang out, and a chilling cold swept across the battlefield.

It raised the monsters that had fallen moments ago and the ones falling even now.

—Krr. Grrrk.

Slow, rasping cries.

An eerie light glimmered deep within their eyes.

The undead army, reborn as new beings at the edge of death, charged without a moment’s hesitation at the monsters surging in from every direction, obeying their king’s command.

—Kraaaaaa!

—Grr. Uh. Uh. Uh!

*Thud. Kraaang!*

The roars of monsters that were alike yet different tangled together, and weapons swung with force slammed into one another’s bodies.

But unlike the monsters still alive and therefore capable of feeling pain, the undead were creatures that had forgotten pain along with death.

—Graaah.

*Crunch! Splatter!*

Outnumbered? It didn’t matter.

Even with their limbs cut off by weapons flying in from all directions, even with their chests pierced through, they kept moving to the very end.

The Skeleton King had given them only one goal.

Before the magical power he had bestowed upon them ran out, before they met their second death, they had to create another soldier.

*Crack!*

—Kyaaaah!

A monster with its throat torn out screamed.

The undead body, already missing an arm and a leg, was ripped to shreds by the enraged monsters, but that didn’t matter.

Thanks to that, I—

No, we—had bought a little more time.

“Fire!”

“Fire Wall!”

“Lightning Spear!”

*Fwoooosh.*

Countless bolts of lightning and flames streaked through the air.

Behind the enormous transport vehicle blocking the way like a barricade, the monsters packed in so tightly there wasn’t a gap—like the first day of an E-Mart Black Friday sale—had no choice but to take the sudden barrage of attacks head-on.

*Crackle. KRAAAASH!*

—Kraaaaaa!

—Kgh! Grrrk!

Screams filled the air in every direction.

Lightning seared scales and flesh, while flames seeped through the gaps and burned bones and organs.

Many of the hundreds of monsters thrashing in agony unlike anything they had ever felt even swung their weapons at their own allies.

—Kwoooooo!

Monsters driven into each other by the ferocity of pure instinct.

But I didn’t let my guard down for even a moment.

“Hold formation! Don’t take a single step from where you are!”

At my command, carried by internal energy, the Hunters who had been advancing in the heat of battle, caught up in the excitement of gaining the upper hand, stopped in their tracks.

Battle was momentum. It was flow.

But there was a time to ride that momentum.

Against that enormous force of more than ten thousand, killing just a thousand monsters wouldn’t win this battle in an instant.

Slowly. Carefully.

We had to win while minimizing our losses.

Besides…

*I still can’t see him.*

The bastard who still hadn’t shown himself.

The Prophet.

And the S-rank monsters waiting for their moment amid that sea of monsters—or somewhere in the sky above.

Until we took them down, neither this battle nor the war would end.

*This fight… is only just beginning.*

And at that moment, just as I muttered those words deep in my heart—

*Thud. Thud. Thuuum.*

An immense magical power surged from far away, making the desert tremble.
```
