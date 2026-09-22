<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0640.txt",
      "sha256": "ddee23fb55721a52f4a985b2520f7f4c6a0a49e6cf1bb260a076156c95dbc83e",
      "bytes": 13051
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "18afaba066faa90913c85bcc801c2fd4f0f50d6487a6a58f8cdfb1ba44c2eadd",
      "bytes": 1184
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2e54c7fa9b2504231369591cadd144fe1f3d21672db80e5ee729597516271371",
      "bytes": 197596
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "03676adfc21e2430ed9ad9ee01ca2e3bf43607032cd46d585d8d398df5589cb3",
      "bytes": 560
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "34257251b3499de014d17c3758c3939b73ad5da4535505c806786bb39b362fbb",
      "bytes": 553
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "67a376da0a433bd57ac8cdad27669e1b2d8c26b7eacd72817f0fc0d5daa547bf",
      "bytes": 1702
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2ee77e9a1d5d7d04bc6461137b6bdb37bcf4edf48b220c849a97822225533a4e",
      "bytes": 202599
    }
  ],
  "estimated_tokens": 9492
}
-->

# Durable State Update — Chapter 640

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 640. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 640. Profile updates may replace only one
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
  "chapter": 640,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 640,
    "continuity_sources": [640],
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
    "Jin Taekyung and the Beast Miao King confronted the last surviving Thousand-Year Spider in the Poisonblood Grounds.",
    "The Thousand-Year Spider deliberately lured them into a web-filled battlefield and summoned the surrounding venomous beasts as guards.",
    "Jin Taekyung used One Annihilation with White Flame, three jiazi of Scorching Yang Qi, and hellfire to destroy the summoned army.",
    "The Beast Miao King tore one of the Thousand-Year Spider's legs free after Jin cleared away its guards.",
    "The injured Thousand-Year Spider fell toward the ground, and its survival remains unresolved.",
    "Yayul Cheok is the Bai people's great chieftain and the Palace Lord of the Nanman Beast Palace."
  ],
  "continuity_sources": [
    639
  ],
  "open_questions": [
    "Did the Thousand-Year Spider survive the fall after losing its leg?",
    "Can Jin Taekyung and the Beast Miao King finish the injured Thousand-Year Spider?"
  ],
  "safe_through": 639,
  "temporary_decisions": [
    "Use Sword Demon for 검마.",
    "Use two-headed horn snake for 쌍두각사, black frog for 흑와, and golden bee for 금봉."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 열화문    | **Fire Gate Clan**               |
| 무림맹    | **Murim Alliance**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 중원     | **Central Plains**                               |                                                       |
| 화신귀무   | **Dance of the Fire God and Demon** |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 민첩               | **Agility**                    |
| 몬스터     | **monster**           |
| 길드      | **Guild**             |
| 대사      | **Master** for a senior Buddhist monk                           |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 탈진 | **Exhaustion** | System status effect caused by exhausting all internal energy while severely injured. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 영물 | **spiritual creature** | Known non-human creature contrasted with unheard-of monsters. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 마비 | **Paralyzed** | Status abnormality inflicted by Kraken's Ink. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 흑호 | **Black Tiger** | A colossal black tiger that appears at the Ailao Mountain massacre site. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 독무 | **Poison Mist** | Deep green mist covering the Poisonblood Grounds swamp. |
| 천년지주 | **Thousand-Year Spider** | Monster appearing at the end of the chapter. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 야수묘왕 | 흑호 | hostile pursuer to unknown supernatural beast | you | blunt and furious | Directly challenges the Black Tiger over the massacre. |

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 639
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, and a master among the Ten Kings.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace and is responsible for the forces stationed at Ailao Mountain.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 637
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 639
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

## Korean source

```text
＃640화



일섬(一殲)은 공격하는 대상을 파괴하다 못해 소멸시키는 기술이다.

순간적으로 모든 힘을 끌어올려 몇 배의 힘을 내는 만큼, 무위가 높아질수록 일섬의 위력도 강해진다.

그럼에도 단 한 가지. 치명적인 단점이 있다면…….

삐빅. 삐빅. 삐비빅!



- 당신은 모든 힘을 소진했습니다!

- 주의! 주의! 무리한 능력의 여파는 당신에게 고스란히 되돌아올 것입니다!

- 상태 이상, [내상]이 부여됩니다!

- 상태 이상, [탈진]이 부여됩니다!

- 상태 이상, [빈혈]이 부여됩니다!

- 상태 이상, [마비]가 부여됩니다!

- 상태 이상의 중첩으로, 모든 능력치가 일시적으로 100씩 하락합니다!



더욱 강력해진 위력만큼, 일섬의 여파로 인한 후유증의 강도도 높아졌다는 거다.

‘……아. 빌어먹을.’

감전이라도 된 것처럼 전신이 파르르 떨리고, 또렷하던 시야가 노이즈 낀 화면처럼 흐릿하게 물든다.

수천의 독물들을 잿더미로 만든 대가는 결코 녹록지 않았다.

‘그래도 레벨 업 한 번 정도는 할 줄 알았는데.’

레벨이 높아질수록 얻을 수 있는 경험치의 양도 줄어든다.

절정 고수 한 명에 빌빌거리던 쪼렙 시절이었다면 레벨 업으로 어느 정도 커버가 가능했겠지만, 그릇이 커진 만큼 채워야 할 경험치도 많아진 지금은 그마저도 쉽지 않았다.

“……흡.”

내상과 탈진으로도 부족해서 빈혈에 마비까지. 기절하지 않은 게 용한 상황이다.

어지러운 시야 속에서 신형을 비틀거리던 나는, 간신히 손을 움직여 백염을 지면에 박아넣었다.

푹!

애처로운 모습으로 창에 몸을 지탱하고 있으려니 아직 적천강이 가르쳐 주지 않은 화신귀무(火神鬼舞)가 아쉽게 느껴졌다.

졸라 봤자 돌아올 대답은 뻔하지만.



‘화신귀무? 혹시 단명하는 게 네놈의 장래 희망이냐?’



지나치게 위험하다는 게 그 이유였는데, 어차피 기껏해야 권총과 자동소총의 차이 정도다.

솔직히 이쯤 되면 그전에 일섬 쓰다가 객사할 것 같기도 했다.

물론, 이런 끔찍한 동네에서 객사할 생각이라고는 눈곱만큼도 없지만.

‘그러니까 보험을 든 거고.’

내심 그렇게 중얼거리던 순간, 때마침 고객의 사고를 알아차린 보험 설계사가 허공에서 떨어졌다.

후우웅. 쿵!

육중한 체구의 노인과 크다는 말보다는 거대하다는 표현이 더 어울릴 법한 거미.

숨만 붙은 채 경련하는 천년지주를 쿠션 삼아 지면에 내려앉은 야수묘왕이 붉게 상기된 얼굴로 내게 두 팔을 벌렸다.

“어어. 그거 정말 선 넘는…….”

와락! 뿌득!

“이런 엄청난 놈을 봤나!”

“악! 아악!”

“도대체 어떻게 한 거지? 열화문의 독문 무공인가? 아니면 적 노께서 사사한 최후 절초?”

팡! 팡!

“어어억!”

“이런 괴물 같으니! 보면서도 믿을 수가 없었다!”

“아아아아악! 이 미친놈아!”

“뭣이? 미친놈! 그래! 맞다! 네놈은 중원이 낳은 미친놈이다!”

객사할 뻔했다. 농담이 아니라 진심으로.

그리고 남만이 낳은 미친놈이 마침내 내 몸을 놓아줬을 때, 나는 귓가로 전해지는 슬픈 알림을 들을 수 있었다.

삐빅.



- 상태 이상, [미약한 인대 파열]이 부여됩니다!

- 회복 전까지 [근력]의 능력치가 20 하락합니다!

- 회복 전까지 [민첩]의 능력치가 20 하락합니다!



“…….”

이러니까 닥터 옥토퍼스가 빌런이지.

하지만 이제는 뭐라 말할 힘도 없다. 고통으로 숨을 헐떡인 채 야수묘왕을 노려보던 나는 가까스로 입술을 열었다.

“거미. 거미.”

“거미? 아. 천년지주?”

“빨리. 얼른.”

애처롭게 손짓하는 내 모습에, 야수묘왕이 감탄한 표정으로 고개를 끄덕였다.

“설마 했는데, 천년지주를 이용하여 독혈지를 파악할 셈이었느냐? 확실히 난 놈은 난 놈이군.”

“아, 제발.”

“허허, 알았다. 네 녀석의 부탁대로 멀쩡히 살려서 이리 데려왔…….”

야수묘왕이 헛소리를 이어가려던 그 순간.

“끄으으으응!”

나는 없는 힘을 쥐어 짜내어 간신히 빼든 백염을, 그대로 천년지주의 머리통에 쑤셔 박았다. 랜덤 보험금을 수령하는 환자의 마음으로.

푹!

- 시싯! 끼에에엑!

괴물의 짧은 단말마와 함께 어디선가 울려 퍼지는 천상의 종소리.

띠링. 띠링. 띠링.



- [Lv.119 천년지주]를 처치하셨습니다!

- 희귀한 존재를 처치했으므로 추가 경험치가 주어집니다!

- 레벨 업!

- 손상된 신체가 상당 부분 회복되었습니다!

- 모든 상태 이상이 해제되었습니다!

- 주의! 당신의 몸 상태는 아직 완전하지 않습니다! 약간의 치료와 휴식이 필요합니다!



아, 내가 이 맛에 보험 들지.

독물 한 마리에서 얻을 수 있는 경험치가 개미 눈물이라면, 천년지주는 하늘에서 내리는 소나기다.

수천에 달하는 독물들을 단번에 처치하며 획득한 경험치와 천년지주의 것을 더하자 죽어 가던 몸에 즉시 활기가 돌았다.

“꺼어어억.”

막타 개꿀.

옛 현인들께서는 말씀하셨다. 레벨 업 한 번이면 오병이어 안 부럽다고.

정확히 누군지는 모르겠는데 아무튼 그랬다. 이거 진짜다.

‘어우. 죽다 살았네.’

요양원 문턱에서 간신히 돌아온 나는 전신에 차오르는 포만감을 느끼며 배를 쓰다듬었다.

그리고 다음 순간, 그런 나를 떨떠름한 표정으로 바라보고 있는 한 사람과 눈이 마주쳤다.

“왜요.”

“…….”

“뭐요.”

“…….”

잠시 침묵하던 야수묘왕이 짜게 식은 눈빛으로 입을 열었다.

“도대체 이럴 거면 왜 살려 두라고 한 거냐?”

왜긴. 당연히 경험치 챙겨 먹으려고 한 거지.

하지만 다년간의 좆소 길드 생활은 내게 없던 눈치와 사회성이라는 것을 만들어 주었다.

나는 처연하면서도 딱딱하게 굳은 얼굴로 대답했다.

“이 손으로 직접 복수하고 싶었습니다.”

“뭐라?”

“저 찢어 죽여도 시원치 않을 놈들의 손……이 아니라 점액질과 거미줄에 의해 희생당한 남만 전사들의 복수를.”

“……!”

크게 뜨인 야수묘왕의 눈에서 잔잔한 파문이 일었다.

파르르 떨리는 눈빛으로 말없이 나를 응시하던 그가, 먹먹한 음성으로 입을 열었다.

“음. 도무지 무슨 말을 해야 할지 모르겠군.”

“쉿. 아무 말 하지 말아요. 말하지 않아도 다 알고 있으니까.”

“너, 너 이 녀석!”

로맨틱한 분위기……는 시벌. 꺼져. 헛구역질 나온다.

하지만 한 가지 확실한 것은, 지금 야수묘왕의 얼굴 위로 숨길 수 없는 감동이 번지고 있다는 것이었다.

‘뭐. 결과가 좋으니까 된 건가?’

죄책감까지 느낄 필요는 없다고 생각한다.

남만 전사들의 죽음을 애도하는 것도 사실이고, 몸을 회복할 만한 경험치가 필요했던 것도 사실이니까.

중요한 건 내 발 빠른 변명이 더 좋은 결과를 불러왔다는 거다.

‘이 소식이 남만에 퍼지면, 남만야수궁의 무림맹 가입 확률이 10% 정도는 올라갈지도.’

그러나 한편으로는 마음 한구석이 무거운 것도 사실이다.

불과 두 시진 정도밖에 떨어지지 않은 곳에서, 수백에 달하는 사람들이 몰살당하는 것을 막지 못했다는 죄책감 때문이었다.

‘……젠장.’

입맛이 쓰다.

아마 지금 이 순간에도 현대와 무림 곳곳에서는 무수한 사람들이 죽어 나가고 있을 것이다.

그들의 사인(死因)은 단순한 교통사고일 수도, 몬스터에 의한 죽음일 수도 있다.

무림인이라면 객잔에서 시비가 붙어 칼을 휘두르다 비명횡사할 수도 있겠지.

어쩌면 악인과 맞서 싸우다가 목숨을 잃는 이름 모를 협객도 있을 거다.

나도 알고 있다. 그들 모두를 구할 수 없다는 것 정도는.

하지만 어쩔 수 없게도 나는 사람이고, 나와 같은 사람이 죽는 게 싫다.

더불어 후회를 느낀다. 내가 그 자리에 있었다면, 죄 없는 사람을 살릴 수 있지 않았을까 하는 후회를.

‘큰 힘에는 책임이 뒤따른다.’

어떤 히어로 무비 속에서 들었던 그 대사가, 어느 순간부터 거대한 바위가 되어 내 몸과 마음을 짓누르고 있었다.

모든 정신을 집중해야 할 운기조식 중에서조차 그랬다.

‘어쩌면, 이것 역시 심마(心魔)겠지.’

작은 한숨과 함께 고개를 내저은 나는 천년지주의 사체를 내버려 둔 채 다시 이동하기 시작했다.

지금의 위치보다 더욱 깊숙하고, 은밀한 독혈지의 내부를 향해서.

철벅. 철벅.

나와 야수묘왕의 발걸음은 더욱 조심스러워졌다.

다섯 마리의 천년지주와 엄청난 숫자의 독물들을 처치한 덕분에 사방이 고요한 상태였지으나, 그럼에도 아직 안심하기에는 일렀다.

‘그중에서도 특히, 그놈이 가장 큰 문제지.’

애뇌산의 망령(亡靈).

시스템이 알려준 명칭에 정확히 부합하는 흑호야말로 영 순위 경계 대상이다.

거대한 동체와 바람과도 같은 움직임. 그리고 짧은 순간 느꼈던 강대하면서도 스산한 기운은, 놈이 일반적인 영물이나 독물의 한계를 아득히 벗어난 존재라는 증거였다.

- 놈은 지금쯤 어디 있을까?

나와 같은 사고방식을 하는 사람이 옆에 있다는 건 큰 장점이다.

귓가를 파고드는 야수묘왕의 전음에, 내가 입술을 달싹였다.

- 글쎄요. 하지만 확실한 건, 아직 놈이 독혈지에 있다는 겁니다.

- 좀처럼 이해가 되지 않아서 묻는 것이다. 기껏 우리를 여기까지 유인해 놓고도, 왜 아직까지 나타나지 않았지? 일각 전이었다면 확실히 우리에게 불리한 싸움이 벌어졌을 텐데.

야수묘왕의 말은 틀림없는 사실이었다.

다섯 마리의 천년지주는 지닌 악명(惡名)에 비해 생각보다 손쉬운 상대였고, 수천 마리의 독물도 마찬가지였지만 애뇌산의 망령이 끼어들었다면 상황은 분명 달라졌을 것이다.

‘처음부터 놈이 가세했다면 그럭저럭 붙어 볼 만했겠지. 하지만 내가 일섬을 쓴 직후에 나타났다면…….’

최선의 대처를 했다 치더라도, 매우 힘든 전투가 되었을 것이다.

놈은 강기도 버티는 이빨과 엄청난 속도, 그리고 명칭에 걸맞게 망령처럼 도무지 느껴지지 않는 기척을 지녔으니까.

어쩌면 나와 야수묘왕 중 한 사람이 죽거나, 사지 하나를 놓고 와야 했을 거다.

물론 최악의 경우라면 두말할 것도 없이 둘 다 죽는 결말일 테고.

‘그런데 어째서. 왜 그런 상황에서도 나타나지 않은 걸까.’

정확한 이유는 모르겠지만, 당장 뇌리를 스치는 생각 중 그나마 가능성이 있는 가설은 두 가지뿐이었다.

첫째. ‘후후, 천년지주는 우리 사대 독물 중 최약체에 불과하다.’와 같은 섬나라식 전개.

그리고 둘째.

‘애뇌산의 망령은, 우리를 해칠 생각이 없다.’

조심스럽게 걸음을 옮기면서 고민을 이어 가던 나는, 곧장 두 번째 가설을 삭제했다. 아무리 생각해도 영 가능성이 없어 보였기 때문이었다.

그리고 계속해서 생각을 이어 가기도 전에, 측면과 후방을 경계하며 뒤따라오던 야수묘왕의 두꺼운 손바닥이 내 어깨를 짚었다.

툭.

‘어우, 씨.’

깜짝이야. 심장 떨어질 뻔했네.

순간 놀란 마음을 진정시킨 나는, 이내 그의 손가락이 가리키는 방향을 따라 고개를 돌렸다.

그리고 갈수록 짙어지는 독무와 사방에 우거진 어두운 밀림 너머, 희미하게 흘러나오는 정체불명의 빛을 발견할 수 있었다.

‘혹시?’

더 이상 말이 필요 없었다. 생각보다 본능이 먼저 알려 주었으니까.

사박. 파슥.

그리고 미약한 독성을 머금은 풀숲을 가로질러 빛이 흘러나온 공간에 다다른 우리는, 마침내 눈 앞에 펼쳐진 광경을 확인하고 멍하니 입을 벌렸다.

“이건……!”

희미한 달빛이 비치는 드넓은 늪지대.

그곳에서 우리를 기다리고 있는 것은, 투명한 거미줄에 칭칭 감싸인 채 매달려 있는 수많은 무언가와 새하얀 알들이었다.
```

## Final English reading copy

```markdown
# Chapter 640

One Annihilation is a technique that doesn’t merely destroy its target—it erases it.

Because it momentarily draws out every ounce of power and produces several times the usual strength, the higher the user’s martial attainment, the more powerful One Annihilation becomes.

Even so, it had one fatal drawback…

*Beep. Beep. Beep-beep-beep!*

> **System**
>
> - You have exhausted all your power!
>
> - Warning! Warning! The aftereffects of overusing your abilities will return to you in full!
>
> - Status abnormality: **Internal Injury** applied!
>
> - Status abnormality: **Exhaustion** applied!
>
> - Status abnormality: **Anemia** applied!
>
> - Status abnormality: **Paralyzed** applied!
>
> - Due to the stacked status abnormalities, all stats temporarily decrease by 100!

The more powerful One Annihilation became, the more severe its aftereffects became as well.

*……Ah. Damn it.*

My entire body trembled as if I’d been electrocuted, and my once-clear vision grew hazy, like a screen covered in static.

The price for turning thousands of venomous beasts into ash was anything but small.

*Still, I thought I’d at least level up once.*

The higher your Level, the less EXP you gained.

Back when I had been a low-level nobody who could barely stand up to a single Peak master, leveling up could cover for that weakness to some extent. But now that my vessel had grown larger, I needed far more EXP to fill it, and even leveling up had become difficult.

“……Hng.”

Internal Injury and Exhaustion weren’t enough—I also had anemia and paralysis. It was a miracle I hadn’t lost consciousness.

As I staggered through my dizzy vision, I somehow moved my hand and drove White Flame into the ground.

*Thud!*

As I leaned pitifully against the spear for support, I couldn’t help wishing Jeok Cheongang had taught me the Dance of the Fire God and Demon.

I knew exactly what answer I’d get if I begged him.

*Dance of the Fire God and Demon? Is dying young your life’s ambition?*

That was because it was far too dangerous, but at most, it would be the difference between a pistol and an automatic rifle.

To be honest, at this rate, I felt like I might die far from home using One Annihilation before then.

Of course, I had no intention of dying in a foreign land in a place this horrible.

*That’s why I took out insurance.*

Just as I muttered that inwardly, the insurance agent who had realized his client had gotten into an accident fell from the sky.

*Whoooosh. Boom!*

The heavily built old man landed on the ground using the Thousand-Year Spider—so enormous that “huge” suited it better than “large”—as a cushion while it convulsed with barely any life left in it.

His face flushed red, the Beast Miao King spread both arms toward me.

“Uh, that’s really crossing the line—”

*Wham! Crack!*

“What an incredible bastard!”

“Argh! Aaaagh!”

“How did you do that? Was it the Fire Gate Clan’s unique martial art? Or the final ultimate technique Old Man Jeok taught you?”

*Whap! Whap!*

“Uuuugh!”

“What a monster! I couldn’t believe it even while watching!”

“Aaaaaagh! You crazy bastard!”

“What? Crazy bastard! Yes! That’s right! You’re the madman the Central Plains gave birth to!”

I nearly died far from home.

I wasn’t joking. I mean it.

And when the madman Nanman had given birth to finally let go of me, I heard a sad notification in my ear.

*Beep.*

> **System**
>
> - Status abnormality: **Mild Ligament Tear** applied!
>
> - **Strength** decreases by 20 until recovery!
>
> - **Agility** decreases by 20 until recovery!

“…….”

This was why Doctor Octopus was a villain.

But I no longer had the strength to say anything. Wheezing from the pain, I glared at the Beast Miao King and barely managed to open my lips.

“Spider. Spider.”

“Spider? Oh. The Thousand-Year Spider?”

“Quick. Hurry.”

The Beast Miao King nodded with admiration at my pitiful gestures.

“I wondered if that was what you meant, but are you planning to use the Thousand-Year Spider to figure out the Poisonblood Grounds? You really are something.”

“Ah, please.”

“Haha, all right. Just as you asked, I brought it here alive and well—”

At that moment, just as the Beast Miao King was continuing to spout nonsense—

“Gnnngh!”

I squeezed out the last of my strength, pulled White Flame free, and thrust it straight into the Thousand-Year Spider’s head.

With the heart of a patient collecting a random insurance payout.

*Thud!*

—Ssssit! Kieeeek!

Along with the monster’s short death cry, heavenly bells rang out from somewhere.

*Ding. Ding. Ding.*

> **System**
>
> - You defeated **Level 119 Thousand-Year Spider**!
>
> - Additional EXP has been awarded for defeating a rare entity!
>
> - Level Up!
>
> - The damaged body has been substantially restored!
>
> - All status abnormalities have been removed!
>
> - Warning! Your physical condition is not yet perfect! A little treatment and rest are required!

Ah. This was why I took out insurance.

If the EXP from a single venomous beast was an ant’s tear, then the Thousand-Year Spider was a downpour from heaven.

When I added the EXP from killing thousands of venomous beasts at once to the Thousand-Year Spider’s EXP, vitality immediately flooded back into my dying body.

“Buuuurp.”

Last hit. Sweet.

The ancient sages once said that a single Level Up made the five loaves and two fish look like nothing.

I don’t know exactly who said it, but that was how it went. And it was true.

*Whew. I almost died.*

I had barely turned back from the threshold of a nursing home when I felt fullness rising through my entire body and rubbed my stomach.

Then, the next moment, my eyes met those of someone staring at me with a deeply unimpressed expression.

“Why?”

“…….”

“What?”

“…….”

After a moment of silence, the Beast Miao King opened his mouth with a look of utter disbelief.

“Then why the hell did you tell me to keep it alive?”

*Why else? Obviously so I could harvest the EXP.*

But years of working for a shitty small Guild had given me something I had never possessed before: social awareness and people skills.

I answered with a mournful, rigid expression.

“I wanted to take revenge with my own hands.”

“What?”

“For the Nanman warriors who fell victim to the hands……no, the slime and webs of those bastards I could tear to pieces and still not feel satisfied.”

“……!”

Ripples stirred in the Beast Miao King’s wide-open eyes.

He stared at me in silence with trembling eyes, then opened his mouth in a choked voice.

“Hmm. I truly don’t know what to say.”

“Shh. Don’t say anything. I already know everything without you saying it.”

“You—you little bastard!”

A romantic atmosphere……Fuck that. Go away. It was making me gag.

But one thing was certain: the Beast Miao King couldn’t hide how moved he was.

*Well, I guess it’s fine if the result is good.*

I didn’t think I needed to feel guilty.

It was true that I mourned the deaths of the Nanman warriors, and it was also true that I needed EXP to recover my body.

What mattered was that my quick excuse had led to an even better result.

*If this news spreads through Nanman, maybe the odds of the Nanman Beast Palace joining the Murim Alliance will go up by about ten percent.*

Even so, it was also true that one corner of my heart felt heavy.

I felt guilty because I hadn’t been able to prevent hundreds of people from being massacred less than two shichen away.

*……Damn it.*

My mouth tasted bitter.

Even now, countless people were probably dying throughout the modern world and the Murim.

Their causes of death might be as simple as traffic accidents, or they might have been killed by monsters.

If they were Murim people, they might get into an argument at an inn, draw their swords, and die a violent death.

There might even be some nameless chivalrous warrior who lost their life while fighting an evildoer.

I knew it. I knew I couldn’t save all of them.

But I couldn’t help it. I was human, and I hated seeing people like me die.

And I felt regret, too. Regret that if I had been there, perhaps I could have saved innocent people.

*Great power comes with great responsibility.*

That line I had heard in some superhero movie had, at some point, turned into a massive boulder weighing down my body and mind.

Even while circulating my qi, when I should have been concentrating with all my might, I felt it.

*Perhaps this is a Heart Demon, too.*

With a small sigh, I shook my head and began moving again, leaving the Thousand-Year Spider’s corpse behind.

Toward the deeper, more secluded interior of the Poisonblood Grounds.

*Splash. Splash.*

The Beast Miao King and I became even more cautious with every step.

The area was quiet because we had killed five Thousand-Year Spiders and an enormous number of venomous beasts, but it was still too soon to let our guard down.

*That bastard is the biggest problem of all.*

Ailao Mountain’s Wraith.

The Black Tiger that perfectly matched the name given by the System was our top-priority target for vigilance.

Its enormous body and windlike movements. The powerful yet eerie qi I had felt for that brief moment. All of it proved that the creature was far beyond the limits of an ordinary spiritual creature or venomous beast.

—Where do you think it is now?

Having someone beside me who thought the same way was a major advantage.

In response to the Beast Miao King’s Sound Transmission drilling into my ear, I moved my lips.

—Who knows? But one thing is certain: it’s still in the Poisonblood Grounds.

—That is what I have been wondering. After going to all the trouble of luring us here, why has it still not appeared? If it had shown up fifteen minutes ago, we would certainly have been fighting at a disadvantage.

The Beast Miao King was absolutely right.

The five Thousand-Year Spiders had been easier opponents than their notorious reputation suggested, and the thousands of venomous beasts had been the same. But if Ailao Mountain’s Wraith had joined in, the situation would have been completely different.

*If it had joined the fight from the beginning, we could probably have put up a decent fight. But if it had appeared right after I used One Annihilation……*

Even if we had responded in the best possible way, it would have been an extremely difficult battle.

The creature had teeth capable of enduring Force, incredible speed, and a presence that was impossible to sense, like a wraith befitting its name.

One of the two of us might have died, or we might have had to leave a limb behind.

And in the worst-case scenario, there was no question that we would both have died.

*But why? Why didn’t it appear even under those circumstances?*

I didn’t know the exact reason, but of all the thoughts running through my head, only two hypotheses seemed even remotely possible.

First: the classic island-nation-style plot.

*Heh heh. The Thousand-Year Spider is merely the weakest of our Four Great Venomous Beasts.*

And second—

*The Wraith of Ailao Mountain has no intention of harming us.*

As I continued thinking while carefully moving forward, I immediately struck the second hypothesis from consideration. No matter how I thought about it, it seemed completely implausible.

Before I could continue thinking, the Beast Miao King, who had been following behind while keeping watch over our flanks and rear, placed his thick palm on my shoulder.

*Tap.*

*Oh, shit.*

That scared the hell out of me. My heart nearly fell out of my chest.

After calming my startled nerves, I turned my head in the direction his finger was pointing.

Beyond the Poison Mist growing denser by the moment and the dark jungle thick with trees on every side, I spotted a mysterious light faintly spilling out.

*Could it be?*

No more words were necessary. My instincts had told me before my thoughts could.

*Rustle. Crackle.*

Crossing the grass that carried a faint trace of poison, we reached the space where the light had emerged.

At last, we saw the scene spread out before us and stood there with our mouths hanging open.

“This is……!”

A vast swamp bathed in faint moonlight.

What awaited us there was a great many things hanging from the air, all tightly wrapped in transparent spiderwebs—and pure-white eggs.
```
