<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0487.txt",
      "sha256": "93e1d124777e2c512e94c442fca50b9e924077e56b8dc58721597b4d4ca2c37f",
      "bytes": 13505
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "998e8ca62d1f425e5682dcb14690bbf8ebf0a25d36ae05bbe174f9c3e396169c",
      "bytes": 3339
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "f001922cd56cb48fa60ad335dcf50dba727de4c3009706b1e9f4b2409337b2cb",
      "bytes": 155381
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "e55c9a3b8c569f4fd01030d6f0e44d0582acf3e360a34321efcebcb2f2de707a",
      "bytes": 1006
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "92bea9b3cfaa46cab5da559af72e21c1327bcd3e3297e537ece11fc6ac3352a7",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "671eba38b9af1bc14694bda4bd7dd8a26b0537680b5a1aa2ec22ee98132a4cd7",
      "bytes": 1547
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "688546ee379e0373fad764fcb74cf5b585b9b9c4d205dfaac02eb586f19f31b4",
      "bytes": 844
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "63ce4b4aebacbb0e591d903b8627d7b9b0eb3ce3f0754696b27b28a95a18dd5c",
      "bytes": 649
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4f9a2b6f44f23a401944cbb3ff87467abd5f25164948ba8ba22aebcefbbab70a",
      "bytes": 151253
    }
  ],
  "estimated_tokens": 11514
}
-->

# Durable State Update — Chapter 487

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 487. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 487. Profile updates may replace only one
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
  "chapter": 487,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 487,
    "continuity_sources": [487],
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
    "The fissure at the Water God Dragon site is a mostly nonfunctional Gate: entry is impossible, the Gate Conquest Quest cannot be generated, and faint demonic qi leaks from it.",
    "Taekyung suspects Dark Heaven's regeneration, teleportation, and Moving Formation are manifestations of Magic connected to the Gate.",
    "Taekyung believes the Gate signals collapsing world laws and an approaching disaster, and wonders whether the Lord of Heaven is connected to the dangerous force from his original world.",
    "Taekyung told Jeok that he came from another world, that an evil force from it is linked to Dark Heaven, that the corrupted imugi was their work, and that a fully opened Gate could release monsters.",
    "Jeok trusts Taekyung more deeply than anyone else, despite interpreting Taekyung's attempted explanation of his origin as a drawn-out declaration that he wanted to die.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people; the severely injured Dongting Fisherman may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "Gung Gibang traced the vessel connected to Honglan to Red Cliffs, while Cheongpung reported that Zhuge Feng found the Gate site from the Water God Dragon's memories.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense.",
    "Jeok's innate qi is damaged and steadily diminishing despite the Thousand-Year Snow Ginseng and the Divine Physician's treatment.",
    "Jeok asked Mungyeong to look after Taekyung and teach him useful secret martial arts and the mindset needed for the future.",
    "Hong Dao's prediction of distorted heavenly patterns and a calamity greater than the Great Faction War is being realized, and Jeok fears Taekyung's account of his origin may be true."
  ],
  "continuity_sources": [
    485,
    486
  ],
  "open_questions": [
    "What lies beyond the exposed Gate, why has it lost most of its functions, and why can no Gate Conquest Quest be generated?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations, and how do they relate to the Gate?"
  ],
  "safe_through": 486,
  "temporary_decisions": [
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, and 마법 as Magic.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter.",
    "Render 선천지기 as innate qi and 진원진기 as true-origin qi.",
    "Render 심마 as Heart Demon and 천기 as heavenly patterns.",
    "Render 독문 무공 as secret martial arts and 비급 as martial arts manual."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 쾌풍검    | **Swift Wind Sword**          | Hyuk Mujin     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 게이트     | **Gate**              |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 아마존 | **Amazon** | Region referenced in Taekyung's crude joke. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 청풍 | 미미 | handler_to_companion_snake | Mimi | cheerful-commanding | Cheongpung repeatedly calls and commands the Thousand-Year Poison Horned Snake. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 제갈풍 | senior_martial_artist_to_old_acquaintance | you / ill-mannered brat | blunt, familiar, and teasing | Jeok treats Zhuge Feng as the younger acquaintance he remembers from childhood. |
| 제갈풍 | 적천강 | younger_old_acquaintance_to_legendary_senior | Senior | respectful but relaxed | Zhuge Feng recalls Jeok's earlier visit and addresses him as an old senior. |
| 제갈풍 | 문경 | old acquaintance to revealed legendary assassin | Slaughter Saint | excited and respectful | Zhuge Feng identifies Mungyeong by his established sobriquet after recognizing his identity. |
| 문경 | 제갈풍 | legendary_senior_to_younger_family_head | you; burden | blunt, insulting, and commanding | Mungyeong orders Zhuge Feng onto his back and dismisses his objections. |
| 청풍 | 제갈풍 | young_martial_artist_to_family_head | Great Hero Zhuge Feng | cheerful and polite | Cheongpung addresses Zhuge Feng as 제갈풍 대협, but deliberately mispronounces the name once as 제갈퐁 for comic effect. |
| 제갈풍 | 청풍 | family_head_to_younger_martial_artist | you | familiar and polite | Zhuge Feng uses 자네 while instructing Cheongpung and responding to his advice. |
| 적천강 | 수신룡 | legendary_martial_master_to_dying_spirit_beast | you | wary and trembling | Jeok asks what the Water God Dragon is after witnessing its mental communication. |
| 문경 | 수신룡 | physician_to_dying_spirit_beast | you | guarded and curious | Mungyeong asks whether the Water God Dragon knows him. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 484
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 485
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 486
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 486
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a former assassin who passed the Divine Physician title to his Disciple, and he has reached the Returned to Youth realm.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance who has asked him to look after and instruct Jin Taekyung, and Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 484
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical, disarmingly casual, eccentric, and inventive; he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃487화



게이트의 존재를 확인한 뒤 여러 가지 생각으로 마음이 복잡했던 나지만, 적천강의 도움으로 깔끔하게 지워 낼 수 있었다.

“…….”

아니다. 도움은 니기럴 거. 얼마나 꼼꼼하게 때렸는지 뼈마디가 쑤실 지경이다.

뒤늦게 만난 혁무진은 끙끙거리는 내 모습을 보고 엄지를 척 치켜세웠다.

“이야, 역시 조장님! 그렇게 맞고도 일어나시는군요!”

“무진아.”

“네?”

“좋게 말할 때 엄지 집어넣으렴. 주먹으로 정수리 내려찍어서 엄지 공주 만들기 전에.”

내 근력이면 압축 프레스 쌉가능.

엄지 공주가 정확히 뭔지는 몰라도, 흉흉한 분위기만큼은 제대로 전해진 것이 분명했다.

치켜세웠던 엄지를 잽싸게 회수한 혁무진이 작게 중얼거렸다.

“맨날 나한테만 난리야. 확 그냥 부상으로 쭉 누워 있었으면…….”

“무진아, 뭐라고?”

“조장님께서 무림의 신성으로 급부상! 하셨다는 이야깁니다!”

“…….”

혼이 담긴 구라 보소.

이 정도면 임기응변을 아트의 경지로 끌어올렸다고 해도 과언이 아니다. 문득 애잔해진 나는 혁무진의 어깨를 두드려 주었다.

“그래. 너도 힘내라. 이번 일로 급부상했던데.”

“예? 제가요?”

“응. 오는 길에 저잣거리에서 들었어.”

혁무진 저 녀석이 여기서나 푸대접이지, 태원진가의 북부 고원 평정을 통해 쾌풍검(快風劍)이라는 그럴듯한 별호까지 얻은 무인이다.

게다가 나 같은 우량주와 항상 붙어 다니니 자연스럽게 주가 상승의 길에 접어들 수밖에.

“양민들 대화 들어 보면 거의 뭐, 역전의 용사더라고.”

“큼, 그렇습니까?”

“어. 최소 초절정 고수야. 이 정도면 완전 급부상 아니냐.”

입꼬리를 씰룩거리며 좋아하던 혁무진이 의심스러운 눈빛으로 나를 위아래로 훑었다.

“뭐냐, 그 불손한 눈빛은?”

“급부상했다면서 때린 다음 급 부상당했다. 뭐 그러실 것 같아서요.”

“……아니, 미친놈아.”

괜찮은 시나리오긴 한데. 아무리 그래도 그렇지 내 이미지가 이 정도였나?

‘생각해 보면 그간 많이 때리긴 했지.’

갑자기 동정심이 든다. 얼마나 맞았으면 이 정도 피해의식에 갇혀 있을까.

애잔한 눈빛으로 혁무진을 바라보던 나는 한숨을 푹 내쉬며 입을 열었다.

“아냐. 저잣거리에서 직접 들었다니까.”

“진짜요? 다 걸고?”

“네 불알 두 쪽 건다.”

“오. 진짠가 보네요. 드디어 태원진가가 낳은 풍운아, 쾌풍검 혁무진의 명성이 천하 무림에 울려 퍼지…….”

히죽히죽 웃던 혁무진이 멈칫했다.

“아니, 잠깐만요. 뭔가 이상한데.”

“뭐가?”

“그렇잖아요. 왜 조장님께서 제 불알을 겁니까?”

나는 태연하게 대답했다.

“그야 당연히 네 불알이니까.”

“예? 그게 왜 당연해요?”

“네가 혁무진이니까.”

“이게 뭔 소리야 도대체…….”

표정 한번 볼만하다.

지금까지 내가 혁무진을 대상으로 걸었던 숱한 내기에서 모두 진다면, 불알이 서른 개쯤 달려 있어도 부족하다는 말은 굳이 할 필요 없겠지.

“혹시 하나 떼서 심어 볼 생각 없냐. 혹시 나무가 자랄지도 모르잖아.”

“뭘요.”

“뭐겠어.”

내 시선을 따라간 혁무진이 미친놈 보는 듯한 눈빛으로 대꾸했다.

“그런 나무가 있다는 얘긴 처음 듣는데요.”

“그러니까 네가 최초가 되는 거지.”

“조장님께 양보하겠습니다.”

“됐고. 뭐 하느라 이제야 나타났냐? 아까부터 안 보이던데.”

수신룡이 쓰러진 직후 우리는 두 갈래로 나뉘었다. 그 과정에서 청풍과 혁무진은 제갈풍을 따라갔으니 꼭 이틀 만에 보는 얼굴이다.

내 질문에 혁무진이 손에 들고 있던 그물을 흔들어 보였다.

“그건 뭐야?”

“물고기요. 계속 포획 중이었어요.”

“물고기?”

“예. 어제부터 계속 잡고 있는데, 쉽지가 않네요.”

어, 그래. 당연히 쉽지 않겠지. 물고기 잡는 게 얼마나 힘이 들겠어.

물고기가 펄떡이는 그물과 혁무진을 번갈아 바라보던 나는 작게 고개를 끄덕였다.

“그랬구나. 우리 무진이가 낚시하느라 바빴구나.”

“장난 아니라니까요. 이놈들이 얼마나 난폭하고 힘이 좋은지, 진이 다 빠질 지경…….”

빡!

“억!”

“진이 빠지긴. 충심을 다해 보필해야 할 직속 상관은 내팽개쳐 놓고 와서 낚시나 즐기고 앉아 있어? 널 보는 내 진이 다 빠져!”

머리를 움켜쥔 채 뒷걸음질 치던 혁무진이 버럭 외쳤다.

“아, 생각하시는 그런 게 아니라고요!”

“이 자식이 어딜 함부로 목소리를 높여. 물고기 잡고 있었다며, 인마!”

“낚시가 아니라, 포획이요! 포획!”

“포획? 청 소협, 이 새끼 포획해!”

“앗! 네, 은인!”

주위를 얼쩡거리던 청풍이 잽싸게 달려와 혁무진을 붙들었다.

화산파의 신성이요, 검성의 진전을 이은 초절정 고수가 펼치는 금나수(擒拿手)를 버틸 리가 있나.

나는 속수무책으로 제압당한 혁무진을 내려다보며 엄숙하게 선언했다.

“내일 무림이 멸망하더라도 나는 한 그루의 불알 나무를 심으리.”

“잠깐. 잠깐!”

“묻겠다. 왼쪽 불알이 네 불알이냐, 오른쪽 불알이 네 불알이냐.”

“둘 다 내 건데 뭔 개소립니까!”

“솔직한 녀석이군. 상으로 둘 다 떼 가도록 하겠다.”

“놔! 놓으라고! 이 미친놈들아!”

혁무진의 비명이 울려 퍼진 바로 그때였다.

취릭!

“양지바른 곳에 묻으면 무럭무럭 자라날…… 엇, 깜짝아.”

그야말로 순식간에 벌어진 일.

새하얗고 길쭉한 무언가가 청풍의 품속에서 빛살처럼 뛰쳐나오자, 혁무진을 제압하고 있던 청풍이 즉각 몸을 일으켰다.

“어디 가! 미미야!”

“푸하!”

간신히 청풍의 제압에서 풀려난 혁무진이 바닥에 떨어트린 그물을 삿대질하며 외쳤다.

“포획! 낚시가 아니라 포획! 직접 보시라고요!”

결과적으로 보자면 혁무진의 외침은 무의미한 것이었다.

미미가 청풍의 품속에서 튀어나와 그물로 향한 그 순간부터, 내 시선은 이미 그쪽에 고정되어 있었으니까.

그리고 눈 앞에 펼쳐진 광경을 확인함과 동시에, 한 가지 생각이 뇌리를 스쳤다.

‘산 넘어 산이군.’

취리릭! 콱!

혓바닥을 날름거리며 그물 틈새를 파고든 미미가 물고기의 아가미를 물어뜯는다.

‘저것’을 물고기라고 불러야 하는 건지는 의문이지만.

쿵! 푸드드득!

새빨간 핏빛으로 물든 눈. 톱날처럼 날카로운 이빨에 성인 장정의 팔뚝보다 큰 몸뚱어리.

그리고 꼬리에는, 시벌. 저게 뭐야.

나는 눈을 의심하며 중얼거렸다.

“……가시?”

헉헉거리며 몸을 일으킨 혁무진이 퉁명스러운 목소리로 대꾸했다.

“말귀 못 알아듣는 걸 보면 귀는 어두우신데, 눈은 좋으시네요.”

“미친. 뭔 놈의 물고기가 꼬리에 가시가 달렸어?”

“독문 병기인가 보죠.”

“……개소리할래?”

“아, 말씀드렸잖습니까. 낚시는 무슨 개뿔 같은 낚시. 포획이라니까요, 포획. 저런 놈을 어떻게 낚시로 잡아요?”

“허.”

포획. 다시 들어 보니 저런 놈을 잡기에 그것만큼 잘 어울리는 단어가 없다.

뭐라 구시렁거리며 걸어간 혁무진이 떨어트린 그물을 들어 올렸다. 이제야 안 사실인데, 그물도 그냥 그물이 아니라 철과 쇠가 들어간 철망(鐵網)이다.

“그거, 도대체 뭐야?”

“보시면 아시겠지만, 이놈들 이빨이 엄청 날카롭습니다. 어지간한 그물은 그냥 한번 깨물면 잘려 나가는 수준이라…….”

“아니, 철망 말고. 그 안에 든 놈들 뭐냐고.”

“아.”

철그럭!

철망을 찢을 듯이 거세게 몸부림치는 ‘그것’들을 바라본 혁무진이 눈살을 찌푸렸다.

“일단은 모두들 혈어(血魚)라고 부릅니다.”

“혈어?”

“예. 눈깔이 핏빛이라서요.”

혈어라, 섬뜩한 외관에 어울리는 이름이다. 하지만 나는 저 괴생명체의 정확한 이름을 알고 싶었다.

‘기감 발동.’

쏴아아아, 띠링.

나를 중심으로 뻗어간 [기감]의 물결이 놈들에게 닿자, 시스템 알림과 함께 커다란 몸뚱어리 위로 레벨 창이 떠올랐다.



[Lv.5 변이된 송사리]



- 새로운 어류를 발견했습니다!

- [변이된 송사리]에 대한 정보가 갱신되었습니다!



아이템창



[변이된 송사리]

종류 : 어류

등급 : 無

제한 : 無

설명 : 미약한 마력에 노출되어 탄생한 변이종. 몰라보게 강해진 데다 상당한 독성(毒性)을 띠고 있지만, 막상 요리하여 먹어 보면 맛있을지도.





“…….”

이게 송사리라고?

나는 어지간한 성인 장정의 팔뚝보다 큰 그것을 바라보며 생각했다.

내가 아는 송사리 어디 갔냐.

‘차라리 여기가 동정호가 아니라 아마존이라고 하지.’

우선 물고기 주제에 레벨이 5씩이나 되는 이 괴물이 송사리라는 것에 놀랐고, 존나 세고 독성이 있지만 맛있을 거라는 시스템창의 개소리에 두 번 놀랐다.

막상 먹어 보면 맛있을 거라니. 독이 있다잖아, 이 미친놈들아.

‘그건 그렇고, 역시 원인은 하나밖에 없겠지.’

이건 분명 게이트에서 흘러나온 마력으로 인한 변화가 틀림없다.

비록 수신룡이 제 한 몸을 희생하여 게이트의 마력을 대부분 흡수했다지만, 잔여물까지 어찌할 수는 없었을 테니까.

그리고 불과 한 두시진 전 직접 확인한 바에 따르면, 게이트는 제 기능을 상실했음에도 미약한 마력을 흘리고 있었다.

‘만약에 이런 것들이 천하 곳곳으로 퍼져 나가면 어떻게 되는 거지? 혹시 감염이라도 된다면?’

사실 질문에 대한 답은 이미 알고 있다.

좆 되는 거지, 뭐.

동정호의 지류는 장강으로 이어져 있고, 장강은 광활한 자연 생태계와 수많은 이들이 오가는 해상 교통로다.

내가 뭐 환경단체 소속도 아니니 생태계 파괴는 둘째치고, 만약 감염 성분이 있어서 육지에까지 변이된 생물체가 넘쳐흐르면 그때는 끝장인 거다.

“……아, 돌아 버리겠네.”

“왜 그러십니까?”

“은인. 괜찮으세요?”

“아니, 하나도 안 괜찮아.”

단호하게 대답한 나는 청풍을 향해 고개를 돌렸다.

“청 소협. 이런 놈들이 얼마나 있어?”

“저는 이쪽에 투입되지 않아서 잘 몰라요. 그런데 미미가 좋아해요. 맛있나 봐요!”

어느새 제 몸보다 몇 배는 큰 혈어 한 마리를 꿀꺽 삼킨 미미를 향해, 청풍이 사랑스러워 죽겠다는 눈빛을 흘려보냈다.

“많이 먹어, 미미!”

“……그래. 당신한테 물어본 내가 등신이지. 그럼 무진아.”

“예. 현재까지 포획한 혈어의 숫자는 백여 마리쯤 되는데, 얼마나 더 있는지는 아직 파악하지 못했습니다.”

정상인의 존재가 이렇게 반가울 줄이야.

나는 감동 어린 눈빛으로 혁무진을 바라보며 재차 물었다.

“제갈풍 대협도 알고 계시고?”

“그럼요. 혈어의 존재를 확인하자마자 입구 부분의 수로를 완전히 폐쇄하도록 지시를 내리신 분이 제갈 대협이십니다.”

“이미 빠져나간 혈어들은?”

“어, 일단은 거의 없는 것 같던데요.”

“뭐?”

[기억의 파편]을 통해 엿본 과거에 의하면, 게이트가 열린 것은 지금으로부터 족히 한 달은 된 시점이다.

지금까지도 게이트가 미약한 마력을 흘리고 있는 걸 봐서는 상당한 물고기들이 변이되었을 텐데…….

“확실해?”

“짐작이긴 한데, 이놈들이 서로 싸우고 있더라고요.”

“싸워?”

“워낙 흉폭해져서, 아군이라는 개념이 없어진 것 같습니다. 지금도 서로 죽고 죽이고 있을걸요?”

“…….”

이걸 좋아해야 하나, 말아야 하나.

흉폭하다는 건 그만큼 위험하다는 건데, 일단 자기들끼리 전쟁이 벌어져서 개체 수를 줄이고 있으니 축하할 일은 맞다.

‘이건 그나마 다행이긴 하네.’

내가 안도의 한숨을 내쉬고 있던 바로 그때였다.

“여기 계셨군요. 진 공자님.”

등 뒤에서 들려온, 맑고 가증스러운 목소리.

고개를 돌리자 어느새 다가온 문경이 나를 바라보고 있었다.

“찾으십니다.”

“바빠. 어른들 일하니까 기다려라.”

“……꼭 데려오라 하셨습니다. 하실 말씀이 있다고.”

“누가?”

살벌한 전음이 귓가를 파고들었다.

- 내가.

“……아.”

그럼 가야지.
```

## Final English reading copy

```markdown
# Chapter 487

After confirming the Gate’s existence, my thoughts had been a mess, but Jeok Cheongang’s help had cleared them right up.

“...”

Actually, screw that. It wasn’t help. He had beaten me so thoroughly that every joint in my body ached.

When I encountered Hyuk Mujin later, he saw me groaning and gave me a thumbs-up.

“Wow, as expected of you, Captain! You can still get back up after taking that kind of beating!”

“Mujin.”

“Yes?”

“Put that thumb away while I’m still asking nicely. Before I pound the top of your head and turn you into Thumb Princess.”

With my Strength, a compression press would be totally doable.

I had no idea what exactly a Thumb Princess was supposed to be, but the murderous atmosphere had clearly gotten through to him.

Hyuk Mujin hastily lowered his thumb and muttered,

“He’s always picking on me. If only he’d stayed laid up with his injuries...”

“Mujin, what did you say?”

“I was saying that the Captain has risen rapidly to become a Morning Star of the Murim!”

“...”

Look at that heartfelt lie.

It would not be an exaggeration to say he had elevated quick thinking to the realm of art. Feeling a sudden pang of pity, I patted Hyuk Mujin on the shoulder.

“Yeah. You hang in there, too. You’ve been shooting up lately.”

“Me?”

“Yeah. I heard it in the marketplace on the way here.”

Hyuk Mujin might be treated like a nobody here, but he was a martial artist who had earned the impressive sobriquet Swift Wind Sword after helping the Jin Family of Taiyuan pacify northern Gaoyuan.

And since he was always walking around with a blue-chip stock like me, his own stock had naturally begun to rise as well.

“Listening to the commoners talk, you sounded like some legendary war hero.”

“Ahem. Is that so?”

“Yeah. At least a Supreme Peak master. If that isn’t shooting up, what is?”

Hyuk Mujin had been grinning happily when he suddenly looked me up and down suspiciously.

“What’s with that disrespectful look?”

“I thought you might say I was on the rise, then hit me and leave me laid up.”

“...You crazy bastard.”

It was a decent scenario, though. But still, was my image really that bad?

*Come to think of it, I have beaten him quite a lot.*

I suddenly felt sorry for him. How many times had he been hit for him to develop this level of persecution complex?

I gazed at Hyuk Mujin with pity, let out a deep sigh, and spoke.

“No. I told you, I heard it in the marketplace myself.”

“Really? You swear on everything?”

“I stake both your balls.”

“Oh. I guess it must be true, then. At last, the fame of the Jin Family’s prodigy, the Swift Wind Sword Hyuk Mujin, has spread throughout the Murim—”

Hyuk Mujin, who had been grinning from ear to ear, suddenly stopped.

“Wait a minute. Something feels wrong.”

“What?”

“Why are you staking my balls?”

I answered calmly.

“Because they’re your balls, obviously.”

“What? Why is that obvious?”

“Because you’re Hyuk Mujin.”

“What the hell does that even mean...”

His expression was a sight to behold.

If I lost every single one of the countless bets I had made involving Hyuk Mujin, saying that even thirty balls wouldn’t be enough would hardly be an exaggeration. There was no need to spell that out.

“Want to cut one off and plant it? A tree might grow.”

“Plant what?”

“What else?”

Following my gaze, Hyuk Mujin answered with the expression of someone looking at a lunatic.

“I’ve never heard of a tree like that.”

“That’s why you’d be the first.”

“I’ll leave that honor to you, Captain.”

“Enough. What were you doing that you only showed up now? You were nowhere to be seen earlier.”

Immediately after the Water God Dragon fell, we had split into two groups. Cheongpung and Hyuk Mujin had followed Zhuge Feng, so this was the first time I had seen them in exactly two days.

At my question, Hyuk Mujin shook the net he was holding.

“What’s that?”

“Fish. I’ve been capturing them.”

“Fish?”

“Yes. I’ve been catching them since yesterday, but it hasn’t been easy.”

Well, obviously. How hard could catching fish be?

I looked back and forth between Hyuk Mujin and the net, where fish were thrashing around, then nodded faintly.

“I see. Our Mujin was busy fishing.”

“I’m not joking. These things are so violent and strong that they’ve nearly drained me dry—”

*Smack!*

“Gah!”

“You call that draining you dry? You abandoned your direct superior, the person you’re supposed to serve with all your loyalty, and came here to enjoy fishing? Just looking at you is draining me dry!”

Hyuk Mujin staggered backward while clutching his head, then shouted furiously,

“That’s not what you think!”

“You dare raise your voice at me? You said you were catching fish, didn’t you?”

“It wasn’t fishing! It was capturing! Capturing!”

“Capturing? Young Hero Cheongpung, capture this bastard!”

“Ah! Yes, Benefactor!”

Cheongpung, who had been loitering nearby, rushed over and seized Hyuk Mujin.

How could Hyuk Mujin possibly resist the grappling technique of Huashan’s Morning Star, a Supreme Peak master who had inherited the Sword Saint’s legacy?

I looked down at Hyuk Mujin, who had been subdued without the slightest resistance, and solemnly declared,

“Even if the Murim perishes tomorrow, I shall plant a single testicle tree.”

“Wait. Wait!”

“I have a question. Is the left one yours, or is the right one yours?”

“They’re both mine! What kind of bullshit is that?”

“You’re an honest fellow. As a reward, I’ll take both.”

“Let go! I said let go! You crazy bastards!”

That was exactly when Hyuk Mujin’s screams rang through the air.

*Hiss!*

“If we bury it somewhere sunny, it’ll grow nice and strong... Whoa, that startled me.”

It happened in an instant.

Something long and pure white shot out of Cheongpung’s arms like a streak of light. Cheongpung immediately sprang to his feet, releasing Hyuk Mujin.

“Where are you going, Mimi?”

“Phew!”

Finally freed from Cheongpung’s hold, Hyuk Mujin pointed at the net he had dropped on the ground and shouted,

“Capture! Not fishing—capture! See for yourself!”

As it turned out, Hyuk Mujin’s protests were pointless.

The moment Mimi sprang out of Cheongpung’s arms and headed for the net, my gaze had already locked onto her.

And the moment I saw the scene unfolding before me, a single thought crossed my mind.

*One mountain after another.*

*Hiss! Snap!*

Mimi flicked her tongue, slipped between the gaps in the net, and tore into one of the fish’s gills.

*I’m not even sure that thing should be called a fish.*

*Thud! Flap-flap!*

Its eyes were bright blood-red. Its teeth were sharp as saw blades, and its body was larger than an adult man’s forearm.

And on its tail… Fuck. What the hell was that?

“...A spike?”

I stared at it in disbelief and muttered.

Hyuk Mujin, who had gotten back to his feet while panting, answered gruffly,

“You may be hard of hearing when it comes to what people say, but your eyesight is excellent.”

“What kind of fish has a spike on its tail?”

“Maybe it’s a special weapon.”

“...Are you going to keep talking bullshit?”

“I told you, didn’t I? What fishing? Fishing, my ass. It was capturing. Capturing! How could you catch something like that with a fishing rod?”

“Huh.”

Capture. Now that I heard it again, there really was no better word for catching something like that.

Grumbling to himself, Hyuk Mujin walked over and picked up the net he had dropped. I only realized it then, but it wasn’t an ordinary net. It was a metal mesh reinforced with iron and steel.

“What the hell is that?”

“As you can see, their teeth are incredibly sharp. An ordinary net would be cut apart with a single bite—”

“I’m not talking about the net. What are the things inside it?”

“Oh.”

*Clang!*

Hyuk Mujin frowned as the things inside thrashed violently, nearly tearing the metal mesh apart.

“For now, everyone calls them Blood Fish.”

“Blood Fish?”

“Yes. Because their eyes are blood-red.”

Blood Fish. It was certainly a fitting name for their sinister appearance. But I wanted to know the exact name of these grotesque creatures.

*Qi Sense.*

*Whoosh... Beep.*

As the wave of Qi Sense spreading from me reached them, a System notification appeared, and Level windows rose above their massive bodies.

> **System**
>
> **Level 5 Mutated Minnow**
>
> - A new fish species has been discovered!
>
> - Information on **Mutated Minnow** has been updated!
>
> **Item Window**
>
> **Mutated Minnow**
>
> **Type:** Fish
>
> **Grade:** None
>
> **Restriction:** None
>
> **Description:** A mutated species born from exposure to weak mana. It has grown incomparably stronger and possesses considerable toxicity, but it might taste delicious once cooked.

“...”

*This is a minnow?*

I stared at the thing, which was larger than an ordinary adult man’s forearm.

*Where did the minnows I know go?*

*At this point, they might as well tell me this isn’t Dongting Lake but the Amazon.*

First, I was shocked that this monster was a fish with a Level as high as 5. Then I was shocked all over again by the System window’s bullshit saying that it was incredibly strong and poisonous but might taste good.

*It might taste good once cooked? You said it was poisonous, you crazy bastards.*

*Still, there could only be one cause.*

This transformation had undoubtedly been caused by the mana flowing out of the Gate.

The Water God Dragon had sacrificed itself to absorb most of the Gate’s mana, but it couldn’t have done anything about the residue.

And according to what I had confirmed personally just one or two shichen earlier, the Gate was still leaking a faint amount of mana despite having ceased to function.

*What will happen if things like these spread throughout the world? What if they’re contagious?*

I already knew the answer to that question.

*We’d be fucked. That’s what.*

The tributaries of Dongting Lake flowed into the Yangtze, and the Yangtze was both a vast natural ecosystem and a maritime route traveled by countless people.

I wasn’t part of some environmental organization, so the destruction of the ecosystem was a secondary concern. But if some infectious agent caused mutated creatures to flood onto land, then it would be the end of everything.

“...This is driving me insane.”

“Why do you say that?”

“Benefactor. Are you all right?”

“No. Not even a little.”

I answered firmly and turned toward Cheongpung.

“Young Hero Cheongpung, how many of these things are there?”

“I wasn’t assigned to this area, so I don’t know. But Mimi likes them. They must taste good!”

Cheongpung gazed at Mimi with an expression of utter adoration. She had already swallowed a Blood Fish several times larger than her own body.

“Eat lots, Mimi!”

“...Right. Asking you makes me the idiot. Then, Mujin.”

“Yes. We’ve captured around a hundred Blood Fish so far, but we haven’t determined how many more there are.”

I never knew the presence of a normal person could be this comforting.

I looked at Hyuk Mujin with a deeply moved expression and asked again,

“Great Hero Zhuge Feng knows about this too?”

“Of course. As soon as the Blood Fish were discovered, Great Hero Zhuge Feng ordered the waterway by the entrance to be completely sealed off.”

“What about the Blood Fish that already escaped?”

“Well, for now, it seems there are hardly any.”

“What?”

According to the past I had glimpsed through the *Memory Fragment*, the Gate had opened at least a month ago.

Judging by the fact that the Gate was still leaking faint mana, a considerable number of fish should have mutated by now...

“Are you sure?”

“It’s just a guess, but they were fighting one another.”

“Fighting?”

“They’ve become so ferocious that they seem to have lost the concept of allies. They’re probably killing one another even now.”

“...”

*Should I be happy about this or not?*

Their ferocity meant they were dangerous, but since they had started a war among themselves and were reducing their own numbers, it was certainly something to celebrate.

*At least that’s a relief.*

I had just let out a sigh of relief when—

“There you are, Young Master Jin.”

A clear, infuriatingly sweet voice came from behind me.

When I turned around, Mungyeong was already standing there and looking at me.

“They’re looking for you.”

“I’m busy. The grown-ups are working, so wait.”

“...I was told to bring you no matter what. They have something to say to you.”

“Who?”

A murderous Sound Transmission bored into my ear.

—Me.

“...Oh.”

Then I had better go.
```
