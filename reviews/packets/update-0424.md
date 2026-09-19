<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0424.txt",
      "sha256": "352834d9827bd33a89dc9689d951e0e123ae2566b75ec5d16c38d916082c8180",
      "bytes": 14866
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1256b9a73b0db7a1feccd1f5f12fcd6a7bee07b99c335d494fb09cb6d29ca8b6",
      "bytes": 2506
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0e12eea2570dfc83f0e97df6a0595a6340580a0c1c882ecd7dd179ffdc25a624",
      "bytes": 140062
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1d6d62c1298dc7a61a5162bdc441af1cdf917680da35c091f34376ee872e1221",
      "bytes": 533
    },
    {
      "path": "characters/Lei Fei.md",
      "sha256": "4500b8f58c81575757bbd7d840a0f619d324c250b014b056c5c7366b816f00d1",
      "bytes": 893
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fb797c7a5f90c7037bd4d22196ea331dd79f86665bbca56edc53a2f3fb178357",
      "bytes": 129444
    }
  ],
  "estimated_tokens": 9769
}
-->

# Durable State Update — Chapter 424

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 424. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 424. Profile updates may replace only one
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
  "chapter": 424,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 424,
    "continuity_sources": [424],
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
    "Jin's Middle Dantian is open, allowing him to perceive the center and grain of magic and sever spells.",
    "Jin has the Severe Injury and Excessive Bleeding status effects; his Strength, Agility, and Stamina each decreased by 200, and he urgently needs treatment.",
    "The Arch Lich survived Flame-Extinguishing Divine Fist and White Flame, though White Flame remains lodged through its chest and its power is weakened.",
    "The top-grade potion was lost, and Lee Jungryong's subspace pocket, now owned by Jin, was thrown out of reach by Dark Vine.",
    "The Arch Lich has begun creating an incomplete Gate in the ruined city that is taller than a high-rise building and wider than a soccer stadium.",
    "Jin launched One Annihilation at the Arch Lich, which used Blink as the attack reached it; the result remains unresolved.",
    "The Gate threatens Jin's people, including Team Leader Choi, Xiao Shen, the Peace Guild members, and his family.",
    "The Arch Lich commands powerful dark magic and continues to regard Jin as a possible Adversary.",
    "The Skeleton Warlord remains Jin's frightened combat ally and is intensely afraid of the Arch Lich.",
    "The Quest One Who Returned from Death remains active, keeping Login unavailable until the Quest ends."
  ],
  "continuity_sources": [
    423,
    422
  ],
  "open_questions": [
    "What was the result of Jin's One Annihilation after the Arch Lich used Blink?",
    "Can Jin stop or disrupt the enormous incomplete Gate before it becomes a catastrophe?",
    "What is the full extent of the Arch Lich's power, including Blink and its ability to observe or identify Jin?",
    "Is Jin truly the Adversary, and what are the god's machinations connecting him to the king?",
    "What is Asmodeus's current status and location?"
  ],
  "safe_through": 423,
  "temporary_decisions": [
    "Render 중단전 as Middle Dantian and 단중혈 as Tanzhong acupoint.",
    "Render Darkness Hold, Dark Hand, Dark Claw, Dark Vine, Bone Shield, Bone Spear, Gate Open, and Blink as the Arch Lich's named spells.",
    "Render 과다출혈 as Excessive Bleeding and preserve Severe Injury as the System status label for 중상.",
    "Render 염화일로 as Flamefire Path, 일섬 as One Annihilation, 겁화 as hellfire, and preserve White Flame.",
    "Preserve the Arch Lich's archaic, contemptuous register and Jin's profanity while retaining the established wuxia and System terminology."
  ],
  "version": 1
}
```

## Exact glossary matches

| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 스킬               | **Skill**                      |
| 레벨               | **Level**                      |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 몬스터     | **monster**           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 레이페이 | **Lei Fei** | Concealed Chinese S-rank Hunter and head of the Public Security Armed Forces Department in Sichuan Province. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 데스나이트 | **Death Knight** | Undead commander type serving under the Black Knight. |
| 대적자 | **the Adversary** | Ancient human enemy remembered by the Arch Lich. |
| 블링크 | **Blink** | Arch Lich movement spell |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 데스나이트 | 인간 | enemy combatants | human | contemptuous and commanding | Used in the Death Knight's warnings to Jin. |
| 데스나이트 | 로드 | subordinate to commanding lord | Lord | fearful and deferential | The Death Knight calls to the Death Knight Lord after Jin overwhelms the army. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 422
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who has sworn never to kill again.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Lei Fei.md

# Lei Fei (레이페이)

- **Safe through:** Chapter 420
- **Aliases:** None
- **Role:** Lei Fei is a concealed Chinese S-rank Hunter and former head of the Public Security Armed Forces Department in Sichuan Province who recovered his human identity after becoming a level-120 undead Death Knight Lord and died fulfilling his final mission.
- **Personality:** Lei Fei's recovered memories show him as dutiful, honorable, family-oriented, and willing to serve as an unseen guardian.
- **Voice:** His human voice is formal and earnest, becoming warm and playful with family.
- **Relationships:** Wei Fenghu is his maternal uncle who raised him as a son; Lei Fei married an unnamed flower-shop owner and had a daughter, trained alongside Wu Heixing, and was corrupted by the Arch Lich before Jin Taekyung restored his identity.

## Korean source

```text
＃424화



콰아아아아!

푸른 화염을 머금은 와류(渦流)는 막아서는 모든 것을 집어삼켰다.

무너진 콘크리트와 앙상한 철골을 드러낸 건축물. 곳곳에 뒤섞여 널브러져 있던 인간과 몬스터의 사체까지.

그렇게 초고온의 열기는 수많은 것들을 불사르고, 녹여 버렸다.

단 하나.

- 블링크(Blink).

놈을 제외한 모든 것을.

삐빅.



- 스킬, [일섬]을 사용했습니다!

- [공력]을 모두 소진했습니다!

- 모든 것에는 대가가 따르는 법. 당신은 심각한 부상에도 불구하고 과도한 힘을 소모했습니다.

- 상태 이상, [탈진]에 걸렸습니다!

- [근력], [체력], [민첩]이 일시적으로 대폭 하락합니다!



나는 전신에서 힘이 빠져나가는 것을 느꼈다. 귓가를 파고드는 시스템 알림도, 인벤토리 속 스켈레톤 워로드의 외침도 제대로 들리지 않는다.

몸은 물먹은 솜처럼 무거웠고 차갑게 얼어붙은 머릿속에는 한 가지 생각만이 계속해서 맴돌았다.

‘마지막 기회였는데.’

왜, 왜 몰랐나. 짐작하지 못했나.

아크 리치는 분명히 말했다. 전장 곳곳에 심어 둔 패밀리어로 내 모습을 지켜보았노라고.

그렇다면 앞서 오는 길에 리치와 데스나이트들을 상대로 일섬을 썼던 것 역시 염두에 두어야 했다.

확신은 아니더라도, 의심은 했어야 옳았다.

‘병신.’

자조 섞인 실소가 흘러나왔다. 그토록 방심하지 않겠다고 다짐했는데…… 결국 가장 중요한 순간에 가장 큰 실수를 저질렀다.

선택의 여지가 없었다는 건 변명이 되지 못한다. 싸움은 과정이 아니라 결과니까. 그리고 이것이 방심의 결과다.

텅!

손가락 사이로 흘러내린 철창이 지면을 나뒹굴었다. 힘이 풀린 다리가 스르륵 허물어졌다.

무릎을 꿇고 고개를 떨군 내 머리 위로 짙은 어둠이 드리워졌다.

- 너, 인간이여. 섣부른 만용의 대가를 치른 기분이 어떠한가?

간신히 고개를 든 나는 타오르는 붉은 안광과 마주했다. 갈라진 입술 사이로 쥐어 짜낸 음성이 흘러나왔다.

“당연히 좆 같지. 이 시벌 놈아.”

- 무서운 일격이었다. 그것 하나만은 칭찬해 주지.

아크 리치의 음성은 승리감에 젖어 있었다.

비록 순간 이동 마법으로도 일섬을 완전히 피하지는 못했는지 왼쪽 팔이 사라져 있었지만, 결국 이 자리에 승자로 우뚝 서 있는 것은 놈이었다.

마치 죄인처럼 무릎을 꿇은 나를 내려다보는 붉은 안광이 기쁨으로 일렁였다.

- 마지막까지 기다렸지. 인간에게 당하는 수모를 겪으면서도 참고 인내했다. 그리고 마침내…… 이 몸의 승리다.

똑똑하고, 음흉한 놈이다.

내 예상대로 놈은 처음부터 일섬을 기다린 것이 분명했다.

앞서 나는 일섬으로 리치와 데스나이트를 쓸어버리고 레벨 업을 통해 체력을 회복했으나, 놈은 내가 순간적으로 모든 힘을 소진했다는 것을 놓치지 않았다.

- 이제 알겠느냐. 이것이 너의, 인간의 한계라는 것을.

한계.

그 한 단어가 가슴을 깊숙이 파고든다.

그토록 노력했음에도 벗어날 수 없었던 F급이라는 이름의 한계. 시스템을 얻은 뒤 나날이 돌파해 나가던 바로 그 한계.

‘정말 여기까지일까.’

죽도록 노력했다. 나를 위해서, 그리고 내가 사랑하는 사람들을 위해서. 어떤 위험이 들이닥쳐도 이를 악물고 헤쳐 나왔다. 나는, 나는 그렇게 살았다. 그 모든 것들이 한계를 뛰어넘는 과정이었다.

“아직…… 안 끝났어.”

남의 것처럼 낯선, 한 줌의 생기조차 느껴지지 않는 목소리가 입술 사이로 흘러나왔다.

나는 흐릿한 눈으로 아크 리치를 올려다보았다.

- 뭐?

“아직, 안 끝났다고.”

목숨을 건 생사결(生死決)은 둘 중 하나가 쓰러져야 끝난다. 그러니 이 싸움은 아직 끝나지 않았다.

마침내 누군가가 죽었을 때, 마지막에 서 있는 그가 승자일 뿐이다.

나는 몽롱한 의식 속에서 중얼거렸다.

‘인벤토리 오픈. 소환.’

명령어와 동시에 인벤토리에 넣어 둔 창 중 하나가 손아귀에 잡혔다.

아니, 잡았다고 생각한 동시에 놓치고 말았다.

터텅!

재차 깨달았다. 지금의 내게는 더 이상 창을 잡을 힘도, 휘두를 기운도 남아 있지 않다는 사실을.

- 크핫! 크하하핫!

그런 내 모습에 아크 리치가 광소를 터트렸다.

하지만 나는 포기하지 않았다. 포기할 수 없었다.

‘인벤토리 오픈. 소환.’

계속해서 무기를 소환하고.

터텅!

계속해서 무기를 놓쳐도.

‘인벤토리 오픈, 소환.’

터텅!

- 인간이여. 이 어리석고 멍청한 인간이여!

설령 아크 리치가 나를 비웃는다고 해도.

결코 멈추지 않았다.

겸허하게 죽음을 받아들이는 용기? 그런 걸 용기라고 부른다면, 차라리 겁쟁이가 되겠다.

나는…… 반드시 살아남을 것이다. 그것이 지금껏 발버둥 친 내 인생에 대한 마지막 예의고, 정답이라고 믿었다.

‘인벤토리 오픈. 소환.’

바로 그 순간이었다.

띠링.



- [인내]가 대폭 상승합니다.

- 능력치, [인내]가 [의지]로 변화합니다!

- 의지가 강한 이들은 쉽게 꺾이지 않으며, 쓰러지지 않습니다. 그들은 마지막까지 의지를 불태우며 혼신의 힘을 다해 싸울 것입니다.

- 강한 의지는, 때로 한계를 뛰어넘는 힘을 발휘합니다!

- 특수 효과, [불굴]이 발현되었습니다. 일시적으로 모든 능력치가 미약하게 상승하며 피로가 줄어듭니다!



나는 몸속 깊은 곳에서 퍼져 나가는 온기를 느꼈다.

비록 본래 지닌 힘에 비하면 한없이 작지만, 한편으로는 어떤 것보다 따뜻한 힘.

그것은 내 간절함에 대한 시스템의 응답이었고, 마지막 기회였다.

여전히 잘게 떨리는 손아귀로 서늘한 창대를 힘주어 움켜잡았다.

- 너…….

변화를 알아차린 것은 나뿐만이 아니었다.

동물원 원숭이를 바라보듯 날 구경하던 아크 리치의 안광이 크게 뜨여진 그때, 나는 모든 힘을 끌어모아 몸을 날렸다.

한없이 느린 세상 속에서 우뚝 서 있는 놈을 향해 손에 들린 창을 뻗었다.

쐐애애애액!

그리고 창날이 파공성과 함께 바람을 가른 그 순간, 나는 똑똑히 보았다. 초승달처럼 휘어지는 아크 리치의 안광을.

그건 비웃음이었다.

- 블러드 익스플로젼(Blood Explosion).

퍼엉-!

폭발음. 그리고 전신을 휩쓰는 충격.

혼신의 힘을 다해 쏘아지던 신형이 덜컥 굳고, 손아귀에서 미끄러진 창이 비스듬히 지면에 박혔다.

나는 실핏줄이 터져 나간 두 눈을 깜빡였다. 온통 붉게 물든 세상 속, 허공에서 떨어져 내린 끈적하고 축축한 무엇인가가 얼굴에 닿았다.

투둑, 투두두둑.

‘……아.’

피다.

내 전신에서 분수처럼 솟구친 핏물이 소나기가 되어 지상으로 쏟아져 내리고 있었다.

사시나무처럼 떨리는 팔을 들어 올리자 너덜거리는 살갗과 새하얗게 드러난 뼈가 보인다.

블러드 익스플로젼. 피의 폭발.

아득해지는 의식 너머로 스켈레톤 워로드의 외침이 들려 온다.

- ……간, 인간!

도대체 언제부터 소리치고 있던 걸까.

뭐라 대답하고 싶었지만, 내 입술 사이로 흘러나온 것은 대답이 아니라 내장 조각이 섞인 핏물뿐이었다.

“쿨럭.”

눈앞이 어지럽다.

얼굴을 뒤덮은 핏물 사이로 흐릿하게 보이는 아크 리치를 향해 손을 뻗었지만 닿지도 않고 닿을 수도 없었다.

어쩌면 앞으로도 영원히.

- 정신 차려라! 살아야 할 것 아니냐!

그걸 말이라고.

당연히 그래야지. 반드시 살아남아서, 놈을 쓰러트리고 내가 있어야 할 곳으로 돌아가야지.

하지만…….

‘그럴 수 있을까.’

그 순간, 세상이 천천히 기울어지기 시작했다.

아니, 세상은 그대로였고 기울어지는 것은 나였다. 계속되는 출혈과 부상을 이기지 못한 몸뚱어리가 힘을 다해 쓰러지고 있었다.

‘안 돼. 쓰러지면 모든 게 끝장이다.’

이미 부러진 발목으로 신체를 지탱했다.

마치 가시에 찔린 것처럼 희미한 고통은 내가 죽어 가고 있다는 증거였고, 노이즈 낀 라디오처럼 드문드문 들려오는 스켈레톤 워로드의 외침은 아직까지 살아 있다는 증거다.

- ……해라, 인간! 어서!

하라고? 뭘?

- 당장 나를 소……!

이미 터져 나간 고막과 흐릿해지는 의식은 스켈레톤 워로드의 외침을 제대로 받아들이지 못했다.

만약 녀석의 말을 똑똑히 들었다고 해도, 이어지는 아크 리치의 행동을 막을 수는 없었을 것이다.

- 너, 재미있는 물건을 가지고 있더군.

어느새 아크 리치의 손에는 낯익은 물건이 들려 있었다.

나와 수많은 전투를 함께 한 애병, 백염(白炎)이 낯선 이의 손길에 불꽃을 피워 올렸지만, 놈은 뼈마디가 타오르는 와중에도 그저 웃을 뿐이었다.

- 과분한 선물을 받았으니, 이제는 주인에게 돌려주어야겠지.

아크 리치가 팔을 뒤로 젖혔다. 백염의 불꽃을 제압한 강대한 마력이 창날을 향해 휘몰아쳤다.

- 잘 가거라. 새로운 대적자여, 혹은 대적자였을지도 모르는 한낱 어리석은 인간이여.

쐐액!

파공성은 짧았고, 순간은 영원 같았다.

나는 말 없이 섬광처럼 쏘아지는 백염을 바라보았다. 수많은 경우의 수가 뇌리를 스쳤고 마침내 결론을 도출해 낸다.

‘피할 수 없다.’

그렇다면 내게 남은 결말은 하나다. 죽음.

7년 전부터 지금까지 수많은 전투를 치렀지만, 지금만큼 죽음이라는 단어가 가깝게 느껴진 적이 없었다.

할 수 있는 것이라고는 그저 다가오는 죽음을 지켜보는 것뿐.

‘그래, 끝이야.’

담담하게 되뇌던 바로 그 순간.

콰직!

백염의 창날이 뼈를 부수며 가슴 한가운데를 관통했고, 나는 눈을 부릅뜬 채 굳어 버렸다.

고통이 아닌, 경악 때문에.

“……너.”

- 왜, 뭐.

나는 할 말을 찾지 못하고 코앞에서 일렁이는 푸른 안광을 바라보았다.

고작 축구공만 한 크기의 두개골에서, 2미터의 신체로 변화한 스켈레톤 워로드가 퉁명스러운 목소리로 말했다.

- 어떻게 혼자서 나올 수 있었냐고 묻지 마라. 본 사령관도 영문을 모르겠으니까.

“그럼, 도대체 왜?”

마주 선 녀석을 바라보며 물었다.

스켈레톤 워로드의 등을 통해 가슴까지 관통한 창날은 나와 정확히 한 뼘을 두고 멈춰 있었다.

누군가가 막아서지 않았다면 분명히 죽고도 남았을 거리.

녀석은 방금, 스스로 몸을 던져 내 목숨을 구했다.

- ……그것도 모르겠다. 빌어먹을. 이제는 아무것도 모르겠어. 어쩌면 이 검에 홀린 것일지도 모르지.

나는 그제야 스켈레톤 워로드의 손에 들린 검의 정체를 알아볼 수 있었다.

“영웅의 혼.”

레이페이의 유일한 유품이자, 영웅이 될 자격을 갖추지 못한 자는 잡을 수조차 없는 검.

바로 그 [영웅의 혼]이 스켈레톤 워로드의 손에 들려 있었다.

인간도 아닌, 네임드 몬스터의 손에.

- 영웅의 혼이라. 인간이 지은 것치고는 괜찮은 이름이군. 아니, 솔직히 말하자면 멋져. 비록 너무 늦는 바람에 제대로 휘둘러 보지도 못했지만…….

스켈레톤 워로드의 목소리가 사그라들었다. 언제나 또렷하던 푸른 안광에서 서서히 빛이 사라지고 있었다.

이런 상황이 무엇을 의미하는지, 나는 알고 있다.

‘소멸.’

틀림없다. 지금 이 순간에도 백염의 창날에 실렸던 아크 리치의 마력은 스켈레톤 워로드를 빠르게 갉아 먹고 있었다.

“너.”

- 그 이상 말하지 마라. 안 그래도 이미 후회 중이니까.

나는 그 말을 믿지 않았다. 퉁명스러운 말투와는 어울리지 않는, 낮은 웃음소리를 들었기 때문이다.

- 인간. 궁금한 것이 있다.

조금씩 허물어지는 스켈레톤 워로드의 어깨너머로 아크 리치가 다가오고 있었지만, 나는 묵묵히 고개를 끄덕였다.

“뭐든지.”

잠시 머뭇거리던 녀석이 작은 목소리로 물었다.

- 지난번에 했던 말. 혹시 진심이었나?

“지난번이라면 어떤…… 아.”

문득 기억났다. 레이페이의 죽음 직후, 기억나지 않는 자신의 과거에 대해 생각하던 녀석의 모습이.

그리고 그런 모습에 지나가듯 건네었던 한마디가.



‘글쎄, 아마도 내 생각에는 썩 괜찮은 놈이었을 것 같은데.’

‘……어? 혹시 그거 본 사령관에게 한 말인가?’

‘아니. 그냥 혼잣말.’

‘커, 커흠. 그렇지?’



그래서였다. 그것 때문이었다.

모든 기억을 잃은 망령에서 힘을 얻고 깨어난 스켈레톤 워로드에게, 늘 함께 있던 나는 하나뿐인 친구였을지도 몰랐다.

내가 던진 작은 돌 같은 한 마디가, 녀석의 마음이 담긴 연못에 파문을 일으킨 것이다.

‘이런 멍청한.’

그게 뭐라고. 그까짓게 뭐라고 이렇게까지 해야 했나.

순간 말문이 막히고 속에서 뜨거운 것이 올라왔지만 꾹 참았다. 나는 간신히 입을 열어 대답했다.

“당연히 진심이었지.”

- 그래, 그렇구나.

위태롭게 깜빡이던 푸른 안광이 호선을 그린 바로 그 순간. 모든 것을 끝내는 스산한 목소리가 울려 퍼졌다.

- 작별 인사는 끝났나?

“……!”

- 본 익스플로젼(Bone Explosion).

쾅!

본능적으로 두 팔을 교차해 얼굴을 막아낸 나는 전신을 휩쓰는 충격과 함께 튕겨 나갔다.

간신히 몸을 일으켜 세우자 높이 솟구치는 두개골과 산산조각 나는 뼈들이 보였다.

그리고…… 그것이 전부였다.

스켈레톤 워로드의 모습은 그 어디에서도 찾아볼 수 없었다.

푸욱!

허공에서 낙하한 [영웅의 혼]이 지면 깊숙이 박혔다. 마지막까지 검 자루를 놓지 않은 누군가의 손과 함께.
```

## Final English reading copy

```markdown
# Chapter 424

*Kwaaaaaaaaaaang!*

The vortex carrying blue flames devoured everything that stood in its way.

Buildings with their concrete walls collapsed and skeletal steel frames exposed. The corpses of humans and monsters scattered and mixed together throughout the ruins.

The ultrahigh heat burned and melted countless things.

Everything except one.

—Blink.

Everything except him.

*Beep.*

> **System**
>
> - Skill **One Annihilation** has been used!
>
> - All **internal energy** has been consumed!
>
> - Everything comes at a price. Despite your severe injuries, you have expended an excessive amount of power.
>
> - The status effect **Exhaustion** has been applied!
>
> - **Strength**, **Stamina**, and **Agility** have temporarily decreased drastically!

I felt the strength drain from my entire body. I could barely hear the System notification drilling into my ears—or the Skeleton Warlord’s shouts from inside my inventory.

My body was as heavy as waterlogged cotton, and only one thought kept circling through my mind, which had gone cold and numb.

*That was my last chance.*

Why? Why hadn’t I known? Why hadn’t I guessed?

The Arch Lich had clearly said that it had watched me through Familiars planted throughout the battlefield.

If so, I should have taken into account the fact that I had used One Annihilation against the Liches and Death Knights on my way here.

I should have suspected it, even if I couldn’t be certain.

*Idiot.*

A self-deprecating laugh escaped me. I had sworn I would never let my guard down again… and in the most important moment of all, I had made the biggest mistake.

The fact that I had no choice was no excuse. A fight was not about the process but the result.

And this was the result of letting my guard down.

*Clang!*

The iron spear slipped between my fingers and rolled across the ground. My legs, drained of strength, slowly gave way.

As I knelt and lowered my head, a deep darkness fell over me.

—You, human. How does it feel to pay the price for your rash arrogance?

I barely lifted my head and met a pair of burning red eye-lights. A voice squeezed through my cracked lips.

“Of course it feels like shit, you fucking bastard.”

—It was a fearsome strike. I shall at least commend you for that.

The Arch Lich’s voice was steeped in triumph.

It seemed that even its teleportation magic had not allowed it to evade One Annihilation completely. Its left arm had vanished.

But in the end, it was the one standing here as the victor.

The red eye-lights looking down at me, kneeling like a criminal, glimmered with joy.

—I waited until the very end. I held back and endured even the humiliation of suffering at a human’s hands. And finally… victory belongs to me.

Smart. Cunning.

Just as I had expected, it had been waiting for One Annihilation from the beginning.

Earlier, I had swept away the Liches and Death Knights with One Annihilation and recovered my stamina by leveling up. But the Arch Lich had not missed the fact that I had momentarily exhausted all my strength.

—Do you understand now? This is your limit. The limit of humanity.

Limit.

That one word pierced deep into my chest.

The limit called F-rank, which I had been unable to escape no matter how hard I worked. The very limit I had continued to break through day after day after obtaining the System.

*Is this really as far as I go?*

I had worked until I nearly died. For myself, and for the people I loved. No matter what danger came at me, I had gritted my teeth and fought my way through it.

That was how I had lived.

All of it had been a process of breaking through my limits.

“It’s not… over yet.”

A strange voice escaped between my lips, unfamiliar enough to sound as if it belonged to someone else, with not even a trace of life in it.

I looked up at the Arch Lich through my hazy eyes.

—What?

“It’s not over yet.”

A life-and-death duel ended only when one of the two fell.

So this fight was not over yet.

When one of us finally died, the one left standing at the end would be the victor.

I mumbled in my dazed state.

*Inventory open. Summon.*

At the same time as the command, one of the spears in my inventory appeared in my hand.

No—I thought I had caught it, but I dropped it immediately.

*Clang!*

I realized it again.

I no longer had the strength to hold a spear, let alone the energy to swing one.

—Kehat! Kahahahah!

The Arch Lich burst into mad laughter at the sight of me.

But I did not give up.

I couldn’t.

*Inventory open. Summon.*

I continued summoning weapons.

*Clang!*

Even when I continued dropping them.

*Inventory open. Summon.*

*Clang!*

—Human. You foolish, stupid human!

Even if the Arch Lich mocked me.

I did not stop.

The courage to humbly accept death? If that was what people called courage, I would rather be a coward.

I would… survive, no matter what.

I believed that was the final courtesy owed to the life I had struggled through until now—and the right answer.

*Inventory open. Summon.*

It happened at that very moment.

*Ding.*

> **System**
>
> - **Endurance** has increased drastically.
>
> - The attribute **Endurance** has changed into **Will**!
>
> - Those with strong wills are not easily broken, and they do not fall. They will burn their will until the very end and fight with every ounce of their strength.
>
> - A strong will can sometimes produce the power to transcend one’s limits!
>
> - The special effect **Indomitable** has manifested. All attributes temporarily increase slightly, and fatigue is reduced!

I felt warmth spread from deep within my body.

Compared to the power I had possessed originally, it was infinitesimal. And yet, in another sense, it was warmer than anything else.

It was the System’s response to my desperate plea.

My final chance.

With my hand still trembling faintly, I gripped the cold shaft of a spear.

—You…

I was not the only one who noticed the change.

The Arch Lich had been watching me like a monkey at the zoo, but its eye-lights opened wide. At that moment, I gathered every bit of strength I had and threw myself forward.

In a world that had slowed to a crawl, I extended the spear in my hand toward the Arch Lich standing tall before me.

*Fwoooooosh!*

And at the instant the spearhead cut through the air with a piercing roar, I saw it clearly.

The Arch Lich’s eye-lights curved like crescent moons.

It was mocking me.

—Blood Explosion.

*Boom!*

An explosion.

Then a shock wave swept over my entire body.

The body I had launched forward with every ounce of my strength suddenly locked up, and the spear slipped from my grasp and stabbed diagonally into the ground.

I blinked with both eyes, their tiny blood vessels burst. In a world dyed entirely red, something sticky and wet fell from the air and touched my face.

*Drip. Drip-drip-drip.*

*…Ah.*

Blood.

The blood gushing from my entire body like fountains was pouring down to the ground like a rain shower.

I lifted my arm, trembling like an aspen leaf, and saw ragged flesh and stark-white bone exposed beneath it.

Blood Explosion.

An explosion of blood.

Beyond my fading consciousness, I heard the Skeleton Warlord’s cry.

—…Human!

How long had it been shouting?

I wanted to answer, but what flowed between my lips was not an answer. It was blood mixed with bits of my organs.

“Cough.”

My vision spun.

I reached toward the Arch Lich, barely visible through the blood covering my face, but I could neither touch it nor reach it.

Perhaps I never would.

—Get a hold of yourself! You have to live!

Like that needed saying.

Of course I did.

I had to survive, defeat the Arch Lich, and return to the place where I belonged.

But…

*Could I really do that?*

At that moment, the world slowly began to tilt.

No. The world was still, and I was the one tilting.

My body, unable to withstand the continuing bleeding and injuries, was collapsing with all the strength it had left.

*No. If I fall, everything is over.*

I supported myself with the ankle that was already broken.

The faint pain, like a thorn prick, was proof that I was dying. The Skeleton Warlord’s shouts, coming intermittently through the static like a radio with a bad signal, were proof that I was still alive.

—…do it, human! Hurry!

Do what? What?

—Summon me right n—!

My eardrums had already burst, and my fading consciousness could not properly process the Skeleton Warlord’s voice.

Even if I had heard its words clearly, I would not have been able to stop what the Arch Lich did next.

—You possess an interesting item.

At some point, a familiar object had appeared in the Arch Lich’s hand.

White Flame, the treasured spear that had fought alongside me through countless battles, caused flames to flare up in the grasp of a stranger.

But even as its finger bones burned, the Arch Lich merely laughed.

—I have received an extravagant gift. I should return it to its owner now.

The Arch Lich drew its arm back. Powerful mana that had subdued White Flame’s flames surged toward the spearhead.

—Farewell, new Adversary—or perhaps merely a foolish human who might have been the Adversary.

*Fwoosh!*

The sound of the spear cutting through the air was brief, but the moment stretched into eternity.

I silently watched White Flame shoot toward me like a flash of light. Countless possibilities flashed through my mind, and at last, I reached a conclusion.

*I can’t avoid it.*

Then there was only one ending left to me.

Death.

I had fought countless battles from seven years ago until now, but death had never felt as close as it did at this moment.

All I could do was watch it approach.

*Yes. It’s over.*

At the very moment I calmly repeated those words to myself—

*Crack!*

White Flame’s spearhead shattered bone as it punched through a chest, and I froze with my eyes wide open.

Not because of the pain.

Because of the shock.

“You…”

—What?

I could not find the words. I stared at the blue eye-lights flickering right in front of me.

From a skull barely the size of a soccer ball, the Skeleton Warlord had transformed into a two-meter-tall body. In a gruff voice, it said,

—Do not ask how I managed to come out on my own. This commander has no idea, either.

“Then why? Why did you…”

I looked at it as I asked.

The spearhead that had pierced through the Skeleton Warlord’s back and chest had stopped exactly a handspan away from me.

If someone had not blocked it, that distance would certainly have been enough to kill me.

It had just thrown itself in front of me and saved my life.

—…I don’t know that either. Damn it. I don’t know anything anymore. Maybe this sword bewitched me.

Only then did I recognize the sword in the Skeleton Warlord’s hand.

“Hero’s Soul.”

Lei Fei’s only remaining keepsake.

A sword that could not even be held by someone who lacked the qualifications to become a hero.

That very Hero’s Soul was now in the Skeleton Warlord’s hand.

In the hand of a named monster that was not even human.

—Hero’s Soul. That is a decent name for something named by humans. No, to be honest, it is cool. It is a shame I was too late to swing it properly…

The Skeleton Warlord’s voice faded.

The light was slowly disappearing from its blue eye-lights, which had always shone so clearly.

I knew what this situation meant.

*Erasure.*

There was no doubt.

Even now, the Arch Lich’s mana carried on the spearhead of White Flame was rapidly eating away at the Skeleton Warlord.

“You…”

—Do not say anything more. I already regret this as it is.

I did not believe it.

Because I heard a low laugh that did not match its gruff tone.

—Human. There is something I wish to ask.

The Arch Lich was approaching over the Skeleton Warlord’s slowly crumbling shoulder, but I silently nodded.

“Anything.”

The Skeleton Warlord hesitated for a moment before asking in a small voice,

—What you said last time. Were you serious?

“If you mean last time, what are you—ah.”

I suddenly remembered.

It had been right after Lei Fei’s death, when the Skeleton Warlord had been thinking about its forgotten past.

And the words I had casually offered it then.



*“Well, I think he was probably a pretty decent guy.”*

*“…Huh? Were you saying that to this commander?”*

*“No. Just talking to myself.”*

*“Ahem. Right?”*



That was why.

That was what it had been about.

For the Skeleton Warlord, which had awakened from a spirit that had lost all its memories and gained strength, I might have been its only friend—the one who had always been by its side.

A single word I had tossed out like a small stone had sent ripples across the pond that held its heart.

*What an idiot.*

What did it matter? What was so important about that one little thing that it had to go this far?

For a moment, I could not speak, and something hot rose inside me. I forced it back and barely opened my mouth.

“Of course I meant it.”

—Yes. I see.

At the moment the blue eye-lights, flickering precariously, curved into a smile, a chilling voice rang out and brought everything to an end.

—Have you finished saying your farewells?

“……!”

—Bone Explosion.

*Boom!*

I instinctively crossed both arms in front of my face. The shock wave swept across my entire body and sent me flying.

When I barely managed to push myself upright, I saw a skull soaring high into the air and bones shattering into pieces.

And…

That was all.

There was no sign of the Skeleton Warlord anywhere.

*Thud!*

Hero’s Soul fell from the air and plunged deep into the ground.

Along with the hand of someone who had not let go of its hilt until the very end.
```
