<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0800.txt",
      "sha256": "7bbc84d7d01c749716a70943e1e7591eeb3c36b3e0fefb12e7ab7a3c9e277946",
      "bytes": 13858
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "53ec9858e3ec786677b1e34a908a4ae0b870c240dcead43c7ad82720f2e1b801",
      "bytes": 1378
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8c9dc8070fa756b845bf81e2219201805fa9702c6b54e02735af9a47785da09b",
      "bytes": 224512
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8335f494593f587403bef6f5783de6d5055568a12e9e81003690682baadfbad8",
      "bytes": 553
    },
    {
      "path": "characters/Leviathan.md",
      "sha256": "454a8c3480d40aed3fa3d271632915afca0da2854c6b72ced15cce30aad87422",
      "bytes": 666
    },
    {
      "path": "characters/Michael.md",
      "sha256": "1cd804fecd70b23663106c2e22b36379b5220feb26b0f54ac85f999cea34bfb1",
      "bytes": 820
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "42fdbe8e4fcc29b5a8dfc98de4fe3f01827307a1816e676efb4fffaaa8fcccb4",
      "bytes": 707
    },
    {
      "path": "characters/Yamamoto.md",
      "sha256": "23bb4544e86bed18cd6baa9e70937433674a2eaf79e8783b4a34f80fc2b1f1d0",
      "bytes": 574
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3e59cb655c9a73cdf684d32e0a0e00a3e14d3564ec8aecd76d7bc7e8627e892d",
      "bytes": 246930
    }
  ],
  "estimated_tokens": 9189
}
-->

# Durable State Update — Chapter 800

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 800. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 800. Profile updates may replace only one
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
  "chapter": 800,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 800,
    "continuity_sources": [800],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and is pursuing Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "The Prophet is a monster who stopped all ten J1 transport vehicles and absorbed blood and a pale mist from the dead; the nature of this power is unknown.",
    "The Prophet left a message intended to lure Jin; its contents are unknown.",
    "Yamamoto is J1’s sole survivor. He says The Prophet left after reinforcements arrived; Jin suspects Yamamoto tried to flee.",
    "Amir and Hamid lead a group concealed by an unseen veil near a convoy of more than five hundred people; Amir orders them to await The Prophet and the coming holy war."
  ],
  "continuity_sources": [
    799
  ],
  "open_questions": [
    "What message did The Prophet leave for Jin, and where is The Prophet now?",
    "Why did The Prophet spare Yamamoto, and what happened when Yamamoto tried to flee?",
    "What was the pale mist absorbed from the J1 victims, and what is the nature of The Prophet’s power?",
    "Where is Amir’s concealed group, and what is its intended target?"
  ],
  "safe_through": 799,
  "temporary_decisions": [
    "Keep magic distinct from mana.",
    "Render 조센징 as “Chōsenjin,” identifying it as an ethnic slur."
  ],
  "version": 1
}
```

## Exact glossary matches

| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 팀장      | **Team Leader**       |
| 대격변     | **Great Cataclysm**   |
| 귀가      | **your family**                                                 |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 레비아탄 | **Leviathan** | Ancient S-rank sea monster associated with Asmodeus. |
| 미카엘 | **Michael** | Guild Master of Odin Guild. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 야마모토 | **Yamamoto** | Japanese S-rank Hunter named in post-Leviathan media coverage. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 실베르트 | **Silbert** | Family name in Michael Silbert. |
| 마계 | **Demon Realm** | Realm associated with the S-rank monsters and Leviathan. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 799
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Leviathan.md

# Leviathan (레비아탄)

- **Safe through:** Chapter 798
- **Aliases:** None
- **Role:** Leviathan was an ancient S-rank sea monster and ruler of the sea who was killed by Jin Taekyung after the deep-sea hunt, leaving a final warning that the Cataclysm was approaching.
- **Personality:** Ravenous, domineering, and driven by instinctive hunger for magical power and food.
- **Voice:** Its spoken voice is not established; it communicates in Demon Realm language.
- **Relationships:** Leviathan once served the Demon King Asmodeus, its master, and withdrew into the deep sea after Asmodeus fell.

### Michael.md

# Michael (미카엘)

- **Safe through:** Chapter 799
- **Aliases:** None
- **Role:** Michael Silbert was the former Odin Guild Master, executed by Jin Taekyung after the World Hunter Federation’s first resolution.
- **Personality:** Controlled, calculating, condescending, and confident in his intelligence and ability to manipulate events, but increasingly impatient and anxious since learning of Jin Taekyung.
- **Voice:** Polite and conversational when relaxed, but quietly authoritative and coercive when asserting control.
- **Relationships:** Michael personally selected and trained Huginn, commands Odin Guild's hidden alliance, secretly confers with The Prophet, and regards Jin Taekyung's friendship with the monster as his fatal weakness.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 799
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a monster posing as the leader of the revived Hasasin, whose power includes stopping transport vehicles and absorbing blood and a pale mist from the dead.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

### Yamamoto.md

# Yamamoto (야마모토)

- **Safe through:** Chapter 799
- **Aliases:** None
- **Role:** Yamamoto Genji is a Japanese S-rank Hunter and J1’s sole survivor.
- **Personality:** Prideful and easily offended, prone to self-aggrandizement and self-serving assumptions, and cowardly under mortal threat.
- **Voice:** Not established.
- **Relationships:** Jin Taekyung sent Yamamoto on the J1 mission and treated him after the attack, though Jin resents Yamamoto for arriving late during the Leviathan crisis.

## Korean source

```text
＃800화



헌터란 언제나 죽음과 맞닿아 있는 이들이다.

전 세계에 모르는 사람이 없는 S급 헌터든, 길바닥 돌멩이처럼 굴러다니는 F급 헌터든 예외는 없다.

죽음이라는 불운은 누구에게나 평등하게 찾아오는 법이고, 헌터들은 그 사실을 누구보다 익숙해져 있는 사람이었다.

하지만…….

“Holy shit.”

나지막하게 흘러나온 욕설이 모두의 심정을 대변한다.

지금 이 순간 잘게 흔들리는 수십여 쌍의 눈동자에 비치고 있는 것은, 바싹 쪼그라든 이백여 구의 시신이었다.

“빌어먹을. 혹시 우리 중에 단 한 번이라도 이런 미친 광경을 본 사람이 있나?”

팀장의 질문에도 모두가 입을 다물었다. 아니, 대답하는 것마저 잊었다고 표현하는 것이 정확했다.

‘도대체 이게 뭐지?’

비록 후방에서 유해 수습을 맡고 있지만, 그들 역시 한 사람의 헌터다. 목숨이 왔다 갔다 하는 경험은 기본이고 시체라면 지긋지긋하게 봤다.

특히 최근 몇 달간 차례대로 벌어진 일련의 사건들을 통해 얼마나 많은 죽음을 목격했던가.

하지만 그런 이들조차, 지금 이 순간만큼은 등골이 서늘해질 정도의 한기를 느낄 수밖에 없었다.

“……사망한 지 아직 두 시간도 안 지났다고 하지 않았습니까?”

긴 침묵을 깨트리는 누군가의 질문에 팀장이 입술을 깨물었다.

“믿을 수 없겠지만, 맞아. 분명히 그렇게 전달받았어.”

“그럼 둘 중 하나겠군요. 팀장님이 귀가 먹었거나, 전달해 준 사람이 미쳤거나.”

“그럴 수 있겠지. 하지만 둘 다 아니야.”

“글쎄요. 시신 상태를 보니까 족히 두 세기는 지난 것 같은데요. 도대체 어느 미친놈이 겨우 두 시간도 안 됐다고 전달해 준 겁니까?”

“왜, 가서 따지려고?”

“사실 여부 확인은 해 봐야죠. 만약 헛소리를 지껄인 거면 면상에다 한 방 먹여 주고요.”

“좋아.”

어느새 담배 한 대를 꺼내 문 팀장이 침착하게 말을 이었다.

“정 그러고 싶으면 지금 당장 지휘부 막사로 가. 그리고 매직 존슨을 보는 즉시 면상에 주먹을 날려. 자네들 시체는 내가 잘 수습해서 가족들에게 데려다줄 테니 뒷일은 걱정하지 말고.”

“예?”

“아직 안 갔나? 그 미친놈을 찾아서 한 방 먹여 준다며?”

“…….”

헌터들은 할 말을 잃어버렸다.

조금 전만 해도 자신들이 욕하던 미친놈의 정체가 매직 존슨이라는 것 때문이라기보다는, 이 명령이 잘못되지 않았다는 현실에서 오는 충격이 더욱 컸다.

‘그럼, 이게 전부 사실이라고?’

‘빌어먹을. 무슨 일이 벌어지고 있는 거지?’

베테랑 헌터가 되었다는 건, 팬케이크 굽는 냄새보다 피비린내에 익숙해졌다는 뜻이고 이 일을 그만둬도 장의사로 전향해도 될 만큼 끔찍한 광경에 익숙해졌다는 뜻이다.

사지가 잘려 나가고, 몸통이 뜯기고, 머리가 으스러지고…….

이미 질리도록 본 광경이다. 그들이 목격한 시체의 대다수는 몬스터였지만, 한솥밥을 먹던 동료의 것도 적지 않았다.

하지만 죽음에 익숙해진 그들로서도 이런 시체는 처음이었다.

피 한 방울 없이 바싹 말라붙은 이백여 구의 시체.

일련의 상황을 몰랐더라면 아마 백이면 백. 자신들이 유적 발굴에 투입되었다고 착각했을 것이다.

이건 단순한 시체가 아니라 몇백 년간 땅속 깊이 잠들어 있던 미라 같았으니까.

‘제기랄. 귀신에 홀리기라도 했나.’

‘이 상태가 두 시간도 안 됐다고? 그게 말이 돼?’

참혹한 것이 아니다. 단지 그 이상으로 기괴할 뿐이다.

매 순간 전신에 소름이 돋을 만큼. 한 줌의 생기(生氣)조차 찾아볼 수 없는 저 시신에게 한 걸음도 다가설 수 없을 만큼.

동시에 한 가지 의문이 모두의 머릿속을 채웠다.

‘도대체 무엇에 당한 거지?’

누구, 가 아닌 무엇.

감히 예측조차 할 수 없는 미지의 적을 떠올리며 사람들이 침을 꿀꺽 삼킨 그때. 입에 문 담배를 깊게 빨아들인 팀장이 외쳤다.

“Fuck. 언제까지 넋 놓고만 있을 거야! 괜한 생각 그만하고 당장 움직여! 어서!”

지금 막 잠에서 깨어난 것처럼 화들짝 놀란 헌터들이 그제야 미적미적 움직이기 시작한다.

그리고 떨어지지 않는 발걸음을 억지로 떼어 시신들에게 다가가는 부하들을 바라보던 팀장은, 문득 자신이 아직 담배에 불도 붙이지 않았다는 사실을 깨달았다.

‘……제기랄.’

내심 욕설을 중얼거린 그는 물고 있던 담배를 땅에 내던졌다.

그러나 어느새 바짝 말라붙은 입술을 매만지는 손길은 잘게 떨리고 있었다.



* * *



“소문이 퍼지고 있습니다.”

최 팀장이 무거운 얼굴로 입을 열었다.

“모두가 두려워하고 있어요. 전사자들의 시신에 관한 이야기가 은연중에 나돌고 있습니다.”

“…….”

“더 늦기 전에 뭔가 조치를 취해야 합니다. 이대로라면…….”

자연스럽게 흐려지는 말꼬리. 하지만 이미 앞서 들은 말로도 뜻을 이해하기에는 충분하다.

나는 마음속으로 최 팀장이 끝맺지 못한 한 마디를 이었다.

‘제대로 움직이기도 전에, 내부부터 무너지겠지.’

미카엘 실베르트와 같은 배신자의 등장을 이야기하는 것이 아니다.

이건 군대를 움직이는 가장 근본적인 힘. 사기(士氣)를 뜻한다.

‘두려움에 잠식당하고 있다. 그것도 급속도로 빠르게.’

이 세상에는 최대한 막아 보려 해도 막을 수 없는 종류의 일이 존재한다.

바로 지금처럼.

“목격자가 너무 많았습니다. 입단속을 실시했지만, 역시 소문을 막기에는 한계가 있었던 것 같습니다.”

함구령에도 한계가 있는 법.

야마모토 겐지가 소속되어 있던 J1 팀은 기괴한 형태로 몰살당했고, 나보다도 먼저 현장에 도착해 있던 이들의 머릿수만 무려 수백이다.

내 이름이 가지는 권위로도 그들 모두의 입에 자물쇠를 채울 수는 없었다.

사람의 감정.

특히 두려움과 같은 종류의 부정적인 감정은 통제할 수 없는 불가항력과 같으니까.

하지만 더욱 큰 문제는, 산전수전 겪은 베테랑 헌터들마저 두려워하는 그 소문이 단순한 헛소문이 아니라는 사실이다.

“그리고 아직까지 그리 큰 호응을 얻고 있지 않습니다만…….”

잠시 머뭇거리던 최 팀장이 한숨과 함께 말을 이었다.

“일각에서는 살이 덧대어져 말도 안 되는 헛소문도 나오고 있습니다.”

“헛소문이라면 어떤?”

“선지자가 정말 신의 선택을 받은 대리인이라거나. 혹은 마왕 아스모데우스와 같은 초월적 존재…….”

쾅!

“개소리!”

고함과 동시에 자리를 박차고 일어난 매직 존슨이 사납게 눈을 부라렸다.

“말해, 최. 도대체 어느 놈들이 그런 정신 나간 소리를 지껄이는 거지?”

“앞서 말했듯이 큰 호응을 얻진 못하고 있고, 떠도는 말들 중 하나라 누구라고 특정할 수도 없습니다. 다만 문제는 그 헛소리를 진심으로 믿는 극소수의 사람들이 존재한다는 겁니다.”

“지금이 어떤 세상인데 그따위 미신 같은 이야기를…… 빌어먹을.”

뭐라 말을 이으려던 매직 존슨이 거친 욕설과 함께 입을 다물었다.

아마 저 거구의 대마도사도 말하는 도중에 잠시 잊고 있던 사실을 깨달은 것이 분명했다.

헌터라는 족속은 세상 그 누구보다 미신에 집착한다는 것을.

어찌 보면 당연한 일이다. 헌터가 된 이유가 무엇이건 간에 결국 인간이라면 누구나 생존 욕망를 지니고 있으니까.

일반인이라면 꿈도 꾸지 못할 막대한 부, 인류를 지키는 검과 방패라는 명예.

그러나 헌터가 무엇보다 우선시하는 가치는 바로 생존이다.

스포츠 선수들도 이해할 수 없는 희한한 루틴을 꼬박꼬박 지키고, 단순하고 유치한 미신에 매달리는데 목숨 걸고 싸우는 헌터들은 어떻겠나.

전자가 선수 생명을 지키기 위해 미신을 신봉한다면, 헌터들은 말 그대로 생명이 달린 문제다 보니 예민하게 받아들일 수밖에 없었다.

더군다나 지금까지 그 누구도 겪어 보지 못한, 미지(未知)의 현상을 마주했을 경우에는 더더욱.

“아무리 그래도 마왕이라니. 죄다 멍청한 인간들뿐이군.”

나는 기가 찬 표정으로 중얼거리는 스켈레톤 킹을 물끄러미 바라보았다.

이미 앞서 여러 차례나 비슷한 시선을 받은 녀석은 그 의미를 즉각 깨닫고 미간을 찌푸렸다.

“말했잖나. 이 몸도 모른다고.”

이건 원했던 대답이 아니다.

나는 실망감을 애써 억누르며 입을 열었다.

“그랬지. 그래서 생각할 시간을 줬고.”

“……빌어먹을. 나도 진심으로 궁금하다. 선지자라는 그놈이 도대체 어떤 존재인지.”

한숨을 푹 내쉰 스켈레톤 킹이 말을 이었다.

“하지만 모르는 걸 어쩌란 말이냐. 이 몸은 너희가 게이트라 불리는 그곳에서 처음으로 의식이라는 걸 되찾았다. 그 이전의 기억은 전부 흐릿해. 아니, 그런 건 기억이라 부를 수도 없지.”

“단편적인 것도?”

“어둡고, 불길한 공간. 내가 떠올릴 수 있는 것들은 그것이 전부다. 아마 그곳이 마계(魔界)겠지. 게이트 너머에 있는 또 다른 세상. 그렇지 않느냐?”

이건 누구도 대답할 수 없는 질문이다. 나뿐만 아니라 매직 존슨. 아니, 인류의 누구조차 마찬가지다.

마왕 아스모데우스가 이 세상에 강림한 이래, 차원 저 너머에 존재하는 죽음의 땅은 존재가 알려짐과 동시에 베일에 가려졌다.

그곳에 무엇이 존재하는지. 어떤 재앙이 살아 숨 쉬는지 단 한 번도 알려진 바가 없다.

그리고 그건 마계를 통해 게이트로 흘러들어온 스켈레톤 킹조차도 예외는 아니었다.

“이 몸이 알고 있는 사실은 극히 일부일 뿐이야. 내가 이 세상에 발을 디딘 이후로 가장 놀랐던 게 뭔지 아나?”

나는 반사적으로 대답했다.

“클럽?”

“……네놈은 평소에 이 몸을 어떻게 생각해 왔던 거냐?”

“불법 밀입국자. 병신. 고자.”

짜게 식은 눈빛으로 나를 바라보던 스켈레톤 킹이 한숨을 푹 내쉬었다.

“빌어먹을. 그래, 물론 그것도 끝내주게 놀라웠지. 하지만 가장 신기했던 건 너희 인간들이 만든 몬스터 대백과 사전이었다.”

“뭐?”

“그걸 보며 처음으로 깨달았다. 이토록 다양한 형태의 몬스터가 존재한다는 것을. 그때까지 내가 알고 있던 건 뼈다귀에 붙은 살점 정도였던 거지.”

“……!”

“하지만 오랜 시간 동안 몬스터에 대해 연구해 왔던 너희 인간들도 아직 모든 것을 밝히진 못했지. 그렇지 않나?”

매직 존슨이 굳은 얼굴로 대답했다.

“사실이야. 몬스터를 연구하는 것에도 한계가 있었으니까.”

이제는 역사 교과서에나 나오는 이야기다.

인류는 대격변 이후에도 더 많은 데이터베이스를 원했고, 종전 직후 헌터들의 역할은 몬스터의 사냥이 아닌 포획이었다.

그리고 이어진 해부를 동반한 온갖 실험들.

하지만 그것으로는 부족했다. 이 세상에는 고블린 같은 하급 몬스터만 있는 것이 아니었으니까.

“상위 몬스터를 포획하려 할수록 희생이 커졌지. 나를 포함한 S급 헌터들이 대거 나섰지만…… 항상 성공으로 이어지진 않았어.”

“그렇다는 건.”

“가장 중요한 타겟이었던 최상위 몬스터 중에는 레비아탄이나 아크 리치처럼 완전히 사라진 네임드도 있었고, 또 드래곤처럼 개체 수가 아주 적은 몬스터들도 존재했거든. 그런 것들은 미처 파악하지 못했지.”

나는 문득 중얼거렸다.

“선지자도 그중 하나일 가능성이 높겠군요.”

“그래. 만약 짐작대로 놈이 정말 몬스터라면…… 틀림없이 우리가 밝혀 내지 못한 최상위 네임드 중 하나일 거야.”

매직 존슨이 가라앉은 목소리로 말을 이었다.

“그리고 단언컨대, 나는 대격변부터 지금까지 이런 종류의 능력을 가진 놈은 단 한 번도 본 적이 없어.”

그야말로 미지의 존재다.

정체도, 능력도 모르는.

그리고 밝혀지지 않은 적과 맞서 싸우는 건 가장 멍청하고 미친 짓이다.

물론, 그 미친 짓을 수없이 해 온 것이 나였고.

“그럼, 남은 선택지는 결국 하나밖에 없네요.”

툭 내뱉은 한 마디에 모두의 표정이 무겁게 가라앉는 것이 보인다. 나는 만류의 목소리가 나오기 전에 말을 이었다.

“곧바로 출정합니다. 반드시 그 새끼 면상을 봐야겠어요.”

한 마디.

선지자가 야마모토 겐지를 통해 내게 전한 그 한 마디를 이정표 삼아 놈의 뒤를 쫓을 것이다.

돌이킬 수 없는 재앙이 일어나기 전에.

설령…… 그것이 함정일지라도.
```

## Final English reading copy

```markdown
# Chapter 800

Hunters were always close to death.

It didn’t matter whether they were S-rank Hunters known to everyone in the world or F-rank Hunters who were as common as stones in the street. No one was exempt.

The misfortune of death came equally to everyone, and Hunters were more accustomed to that fact than anyone.

But…

“Holy shit.”

The low curse spoke for everyone.

Reflected in dozens of pairs of eyes, trembling slightly in that moment, were more than two hundred corpses, shriveled nearly to nothing.

“Damn it. Has anyone here ever seen anything this insane, even once?”

Everyone fell silent at the Team Leader’s question. No—that wasn’t quite right. They’d even forgotten how to answer.

*What the hell is this?*

They might have been assigned to recover the dead in the rear, but they were Hunters all the same. They’d had more than their share of life-or-death experiences, and they’d seen enough corpses to last a lifetime.

Especially after the series of events that had unfolded one after another over the past few months. How many deaths had they witnessed?

And yet, even they couldn’t help feeling a chill run down their spines at that moment.

“……You said they’d been dead for less than two hours, didn’t you?”

The Team Leader bit his lip at someone’s question, which broke the long silence.

“It’s hard to believe, but yes. That’s exactly what I was told.”

“Then it has to be one of two things. Either you’ve gone deaf, Team Leader, or the person who told you is insane.”

“That could be. But neither is true.”

“Maybe not. But looking at these bodies, I’d say they’ve been dead for at least a couple of centuries. What kind of lunatic told you they’d been dead for less than two hours?”

“What, you planning to go argue with them?”

“We ought to check whether it’s true. And if they were talking nonsense, I’ll punch them right in the face.”

“Fine.”

The Team Leader had already taken out a cigarette and put it between his lips. He continued calmly,

“If you really want to do that, go to the command tent right now. The moment you see Magic Johnson, punch him in the face. I’ll take care of your bodies and deliver them to your families, so don’t worry about what happens afterward.”

“What?”

“Are you still here? You said you were going to find that lunatic and punch him.”

“……”

The Hunters were at a loss for words.

It wasn’t so much that the lunatic they’d just been cursing was Magic Johnson. The greater shock came from the realization that the order itself wasn’t wrong.

*So it’s all true?*

*Damn it. What’s going on?*

Becoming a veteran Hunter meant getting used to the smell of blood instead of the smell of pancakes cooking. It meant growing accustomed to sights so gruesome that, even if you quit, you could switch careers and become an undertaker.

Limbs torn off, torsos ripped open, heads crushed…

They’d seen it all more times than they could count. Most of the corpses they’d encountered belonged to monsters, but plenty had belonged to comrades they’d shared meals with, too.

Even so, they’d never seen corpses like these.

More than two hundred bodies, dried out without a single drop of blood.

If they hadn’t known the circumstances, every last one of them would have thought they’d been sent to excavate ruins.

These weren’t just corpses. They looked like mummies that had been buried deep underground for centuries.

*Damn it. Have we been bewitched?*

*They’ve been like this for less than two hours? How is that possible?*

It wasn’t gruesome. It was simply more bizarre than that.

Every moment sent goose bumps crawling over their bodies. They couldn’t take even one step toward those corpses, with not a trace of life left in them.

At the same time, one question filled everyone’s mind.

*What did this to them?*

Not *who*. *What*.

As everyone swallowed hard at the thought of an unknown enemy they couldn’t even begin to predict, the Team Leader took a deep drag on his cigarette and shouted,

“Fuck! How long are you going to stand there staring? Stop wasting time thinking about it and get moving! Now!”

The Hunters jolted as if they’d just woken up, then finally began to move, sluggishly.

Watching his subordinates force their reluctant feet toward the corpses, the Team Leader suddenly realized he still hadn’t lit his cigarette.

*……Damn it.*

He cursed to himself and threw the cigarette from his mouth onto the ground.

But his hand, now brushing over his parched lips, was trembling slightly.

* * *

“Rumors are spreading.”

Team Leader Choi spoke, his face grave.

“Everyone’s afraid. Word about the fallen Hunters’ bodies is going around under the table.”

“……”

“We need to do something before it gets any worse. If this continues…”

His voice trailed off naturally. But what he meant was already clear from what he’d said.

I finished the sentence Team Leader Choi couldn’t.

*We’ll fall apart from the inside before we even get moving.*

This wasn’t about another traitor like Michael Silbert emerging.

This was about the most fundamental force that kept an army moving: morale.

*Fear is eating away at them—and fast.*

There were some things in this world that you couldn’t stop, no matter how hard you tried.

Like this.

“There were too many witnesses. We ordered them not to talk, but it seems there was a limit to how much we could contain the rumors.”

Even an order to keep quiet had its limits.

The J1 team Yamamoto Genji belonged to had been wiped out in a bizarre fashion, and there were hundreds of people who’d reached the scene before I did.

Even the authority my name carried wasn’t enough to lock every one of their mouths.

People’s emotions.

Negative emotions like fear were almost impossible to control.

But the bigger problem was that the rumors frightening even veteran Hunters who’d been through hell and back weren’t baseless nonsense.

“And although they haven’t gained much traction yet…”

Team Leader Choi hesitated for a moment, then continued with a sigh.

“Some people are adding things to the story and spreading absurd rumors.”

“What kind of rumors?”

“That The Prophet really is God’s chosen representative, or some transcendent being like the Demon King Asmodeus…”

Bang!

“Bullshit!”

Magic Johnson shot to his feet with a shout and glared viciously.

“Tell me, Choi. Who the hell is spreading this deranged crap?”

“Like I said, it hasn’t gained much traction, and it’s only one of the rumors going around, so we can’t identify anyone in particular. The problem is that a tiny number of people truly believe it.”

“What kind of world is this, that people are going around believing in that kind of superstition… Damn it.”

Magic Johnson started to say something, then shut his mouth with a rough curse.

The hulking Grand Mage had clearly just remembered something he’d momentarily forgotten.

That Hunters were more obsessed with superstition than anyone else in the world.

In a way, it was only natural. Whatever reason they had for becoming Hunters, every human being wanted to survive.

The vast wealth an ordinary person could only dream of, the honor of being humanity’s sword and shield.

But the value Hunters put above all else was survival.

Even sports players followed all kinds of strange routines that no one else could understand, clinging to simple, childish superstitions. What about Hunters, who fought with their lives on the line?

If athletes believed in superstitions to protect their careers, Hunters couldn’t help taking them seriously when their very lives were at stake.

Especially when they faced an unknown phenomenon that no one had ever encountered before.

“Calling him a Demon King, of all things. They’re all idiots.”

I looked at the Skeleton King, who muttered in disbelief.

He’d already gotten a similar look from me several times, so he immediately understood what it meant and furrowed his brow.

“I told you. I don’t know either.”

That wasn’t the answer I’d wanted.

I suppressed my disappointment and spoke.

“Right. That’s why I gave you time to think.”

“……Damn it. I’m genuinely curious, too. What the hell is that guy called The Prophet?”

The Skeleton King let out a deep sigh and continued.

“But what do you expect me to do if I don’t know? I first regained consciousness in that place you call a Gate. Everything before that is blurry. No, I can’t even call it a memory.”

“Not even fragments?”

“A dark, ominous place. That’s all I can recall. That must be the Demon Realm, I suppose. Another world beyond the Gates. Isn’t that right?”

It was a question no one could answer. Not me, not Magic Johnson—not anyone in humanity.

Ever since the Demon King Asmodeus descended into this world, humanity had known that a land of death existed beyond the dimensions—but the place itself remained shrouded in mystery.

No one had ever learned what existed there, or what calamities lurked within.

And that was true even of the Skeleton King, who had come through a Gate from the Demon Realm.

“What I know is only a tiny fraction. Do you know what surprised me most after I set foot in this world?”

I answered without thinking.

“Clubs?”

“……What have you thought of me all this time?”

“Illegal immigrant. Dumbass. Eunuch.”

The Skeleton King gave me a look that had gone completely cold, then sighed deeply.

“Damn it. Sure, that was incredible too. But what amazed me most was the monster encyclopedia your humans made.”

“What?”

“That was when I first realized there were so many different kinds of monsters. Until then, what I knew about monsters amounted to a scrap of flesh on a pile of bones.”

“……!”

“But even you humans, who’ve spent so long researching monsters, haven’t uncovered everything. Isn’t that right?”

Magic Johnson answered with a grim expression.

“That’s true. There were limits to what we could learn by studying monsters.”

It was the kind of story that appeared only in history textbooks now.

Even after the Great Cataclysm, humanity wanted more data. In the period immediately after the war ended, Hunters weren’t hunting monsters so much as capturing them.

Then came every kind of experiment imaginable, including dissections.

But that wasn’t enough. Not every monster in the world was a low-level one like a goblin.

“The losses mounted the more we tried to capture high-level monsters. A large number of S-rank Hunters, myself included, joined the effort, but it didn’t always succeed.”

“Which means…”

“Among the highest-level monsters we most wanted to target, some Named monsters like Leviathan and the Arch Lich had disappeared completely. And there were monsters like dragons, with very few individuals. We weren’t able to learn much about those.”

I murmured,

“Then The Prophet could be one of them.”

“Right. If he really is a monster, as we suspect… he must be one of the highest-level Named monsters we failed to identify.”

Magic Johnson continued in a subdued voice.

“And I can say for certain that, from the Great Cataclysm up to now, I’ve never seen anyone with this kind of ability.”

He was an utterly unknown being.

We knew neither his identity nor his power.

And fighting an enemy whose nature you hadn’t uncovered was the stupidest, craziest thing you could do.

Of course, I’d done that crazy thing countless times.

“Then there’s only one option left.”

At my offhand remark, I saw everyone’s expression grow heavy. Before anyone could try to stop me, I continued.

“We set out immediately. I have to see that bastard’s face.”

One message.

I would use those words The Prophet had sent me through Yamamoto Genji as a signpost and track the bastard down.

Before an irreversible catastrophe struck.

Even if… it was a trap.
```
