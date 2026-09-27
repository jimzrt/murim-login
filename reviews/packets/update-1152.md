<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1152.txt",
      "sha256": "6634df31f0a9e551ed87180087b48dec600aa5fc1c2a3ae49511335decc2fdf4",
      "bytes": 11306
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e21400f42e6b3e2f4d68734f2c82a5ac91a1bd66607980bb72a047ed0e84670e",
      "bytes": 768
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0235b29aa796a689ced157ef803ab836ad2426783b12138adbefa4121422f8ad",
      "bytes": 246740
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "38eece9ea8f18bd2c024e0f18669654bb5590bab77771db495eb98e2055e007d",
      "bytes": 760
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "086dd0005e1c1a65a8c9b775bfb0a1e4fc134619a76bb15f40ddb6e22d4198e5",
      "bytes": 292572
    }
  ],
  "estimated_tokens": 7403
}
-->

# Durable State Update — Chapter 1152

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
1 and safe_through 1152. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1152. Profile updates may replace only one
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
  "chapter": 1152,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1152,
    "continuity_sources": [1152],
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
    "Furin’s secret Magic Gem-powered weapon, renamed Vladimir, destroys Moscow; Morgoth survives the blast.",
    "Morgoth creates a Dragon Lair over Moscow’s ruins and reveals it to the world through a drone.",
    "Furin warns Morgoth that Jin’s return will mean his end; Morgoth says he looks forward to it."
  ],
  "continuity_sources": [
    1151
  ],
  "open_questions": [
    "What will Morgoth do after revealing the Dragon Lair to the world?",
    "Will Jin return, as Furin warned?"
  ],
  "safe_through": 1151,
  "temporary_decisions": [
    "Render 차르 봄바 as “Tsar Bomba” and the weapon’s new name 블라디미르 as “Vladimir.”",
    "Render 드래곤 레어 as “Dragon Lair.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 헌터      | **Hunter**            |
| 대격변     | **Great Cataclysm**   |
| 귀가      | **your family**                                                 |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 러시아 | **Russia** | Country associated with Sorkovache and the imperial-style sofa. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 대통령 | **President** | Title for Korea's head of state. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 쓰촨 | **Sichuan** | Variant spelling used for the region associated with the pattern Jin recognizes. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 모스크바 | **Moscow** | Russian city used in Taekyung's modern-world comparison. |
| 재생 | **Regeneration** | The masked man's rapid recovery from shattered bones and severe wounds. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 미합중국 | **United States** | Formal Korean reference used during the Defense Minister's imperialist rant. |
| 홍콩 | **Hong Kong** | Location of the Monster Wave mentioned in the media. |
| 흑룡공 | **Black Dragon Duke** | Title in Morgoth's System announcement. |
| 모르고스 | **Morgoth** | The being who answers the summoning. |
| 블라디미르 | **Vladimir** | Furin’s new name for the Magic Gem-powered weapon. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1151
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

## Korean source

```text
＃1152화



현대 사회에 완전한 비밀이란 없다.

어느 곳에나 카메라와 인터넷이 있고, 이를 바탕으로 한 무수한 정보가 전 세계 곳곳으로 퍼져 나가니까.

그리고 때때로 어떠한 종류의 진실은, 알려지지 않는 것이 나을 때가 있다.

열려서는 안 됐을 판도라의 상자처럼.

- 콰아아아아앙!

스피커에도 온전히 담지 못할 만큼 끔찍한 굉음을 마지막으로 화면이 검게 물든 순간.

크렘린 궁 근교에 거주하던 유명 인플루언서의 실시간 스트리밍을 지켜보던 시청자들은 본능적으로 깨달았다.

동시 시청자 1억을 돌파한 이 영상이 지금 막 인터넷 방송계의 역사를 새로 썼으며, 이 놀라운 기록의 주인공이 된 인플루언서를 두 번 다시 볼 수 없으리라는 것을.

- 오, 신이시여.

수 초간 멈춰 있던 채팅창에 불현듯 올라온 단 한 줄의 문구는, 그들이 30여 분 남짓한 시간 동안 보고 느낀 모든 것을 설명하기에 충분했다.

모스크바의 상공을 가로지르던 용의 날개와 송두리째 소멸하는 붉은 광장.

아이러니하게도 그들과 같은 인간의 모습으로 변하여, 앞길을 막아서는 헌터와 군인들을 학살하며 크렘린 궁으로 당당히 걸어 들어가던 그것의 뒷모습.

그리고…….

모스크바를 뒤덮은 재앙.

구구구궁!

수백, 수천 킬로미터 밖으로 뻗어 나간 울림은 직사각형의 화면을 넘어 세상을 뒤흔들었다.

헤아릴 수도 없이 많은 눈과 귀가, 그리고 그보다 많은 카메라가 저 멀리서 번뜩이는 섬광과 거대한 버섯구름을 담았고 이는 곧장 하나의 영상으로 묶여 인터넷에 업로드되었다.

모스크바의 소식을 접한 인류가 느낀, 압도적인 절망과 충격이 고스란히 담긴 제목으로.

- Where is God?

신은 어디에 있는가.

누구도 이 물음에 답하지 못했다.

그 누구도.

다만 모두가 간절히 바랄 뿐이었다.

진정으로 신이 그들을 버렸다면, 자신들을 구원해 줄 누군가가 나타나 주기를.

아니.

한시라도 빨리 깊은 잠에서 깨어나기를.

그리고 너무나도 먼 곳에 있어 목소리조차 닿지 않는 신과 달리, 새로운 시대의 구원자는 오래 지나지 않아 그 간절함에 응답했다.

- 그가 돌아왔습니다.

홀로그램 TV 속, 미합중국의 57대 대통령이 상기된 얼굴로 내뱉은 첫마디에 전 세계가 다시 한번 들끓어 올랐다.



* * *



나에게 있어 현대는 매우 특별한 의미가 있다.

평생을 나고 자란, 잊을 수 없는 고향.

그래서 늘 좋았다.

끊임없는 위험과 사건이 도사리는 무림에 비해, 현대에서는 비교적 편안하게 휴식을 누릴 수 있었으니까.

하지만 언제부터였을까.

망가져 버린 톱니바퀴처럼 모든 것이 어긋나기 시작했다.

그리고 어긋나는 속도와 여파는 내가 상상했던 것 이상으로 빠르고 끔찍했다.

“……그러니까.”

도대체 무슨 말을 해야 할까.

아무런 의미도 없는 뇌까림과 함께 생각을 이어 나갔지만, 새하얗게 물든 머릿속에서는 아무런 말도 떠오르지 않는다.

지금 막 끝난 한 시간 분량의 영상.

나는 이미 재생을 멈춘 홀로그램 영상 속, 카메라를 향해 빙긋 웃고 있는 흑발의 남자를 말없이 바라볼 뿐이었다.

누군가가 이 무거운 침묵을 깨트려 주길 바라면서.

“세 시간 전이라더군.”

낮게 가라앉은 매직 존슨의 목소리에 참았던 한 마디가 메마른 입술을 비집고 흘러나왔다.

“사상자는?”

“…….”

“말해요. 이미 각오하고 있으니까.”

작게 한숨을 내쉰 매직 존슨이 대답했다.

“최소치로 잡아도 이천만 이상.”

“미친.”

“모스크바는 물론이고 인근의 광역권 소도시들까지 휩쓸렸어. 당장 할 수 있는 모든 방법을 총동원해서 조사해 봤지만…….”

말꼬리를 흐린 매직 존슨이 입술을 깨물었다.

“생명 반응이 없어. 아마도 전부 사망했겠지.”

소멸.

순간 머릿속을 스친 단어다.

지금 이 상황을 가장 정확하게 설명할 수 있는 표현이기도 했다.

“블라디미르, 그 빌어먹을 늙은이가 크렘린 궁에 수소 폭탄을 숨겨놨을 줄이야.”

대격변의 시작과 동시에 인류는 아주 중요한 사실 두 가지를 깨달았다.

첫째.

제아무리 철통 보안을 갖추더라도 현대 과학으로는 공간이동 마법을 막을 수 없다.

둘째.

이러한 공간이동 마법은 사람뿐만 아니라 물건도 옮길 수 있다.

이를테면, 전술핵이나 수소 폭탄 같은.

그렇기에 미국과 러시아를 필두로 한 전 세계의 모든 핵보유국은 국제 조약을 맺고 일정 이상의 위력을 지닌 무기를 모조리 폐기했다.

아니, 정확히는 그렇게 알려졌었다.

지금으로부터 세 시간 전, 거대한 버섯구름이 모스크바 상공을 뒤덮기 전까지는.

“러시아는 끝났어.”

맞다.

그리고 러시아를 제외한 다른 국가들에게는, 또 다른 의미의 시작이자 갈림길이 남아있다.

끝까지 저항할 것인가.

혹은 지금이라도 항복하여 목숨을 부지할 것인가.

‘흑룡공(黑龍公) 모르고스.’

나는 마음속으로 뇌까리는 동시에 홀로그램 화면을 응시했다.

마력으로 인해 새카맣게 물든 대지 위.

우뚝 솟아오른 거대한 성을 배경으로 미소 짓고 있는 놈의 얼굴을 눈에 담고 가슴에 새겼다.

‘내가, 쓰러트릴 수 있을까.’

자연스럽게 떠오른 의문과 함께, 나도 모르게 그러쥔 주먹에 힘이 들어간다.

드래곤(Dragon).

과거 단 한 번의 출현만으로도 전 세계를 뒤흔든, 사상 초유의 괴물.

하지만 흑룡공이라는 특별한 이명이 의미하듯, 모르고스는 일반적인 드래곤이 아니었다.

‘강하다. 끔찍할 정도로.’

고개를 돌려 차례차례 바라보았다.

넓은 모니터 룸의 내부를 가득 채운 수십여 개의 홀로그램 영상들을.

날갯짓 한 번으로 빌딩 숲을 무너트리고, 빗발치는 마법을 아무렇지 않게 튕겨 내며 헌터들을 짓밟는 포식자의 모습을.

그리고 마지막 단말마와 함께 죽음을 맞이하는 이들 중에는, 내가 아는 얼굴들 역시 포함되어 있었다.

- 죽어, 죽으라고!

치직거리는 화면 속, 피투성이가 된 여자가 울부짖는다.

이미 처참하게 짓뭉개진 하반신과 쩍 갈라져 내장이 흘러나오는 복부.

그러나 그녀는 퇴각하는 아군의 후미에서 홀린 듯 활시위를 당길 뿐이었다.

화살보다 빠른 속도로 짓쳐 든 용의 발톱이 자신의 두 팔마저 앗아갈 때까지.

콰득!

떨어져 나간 살점과 함께 솟구치는 핏물.

아득한 고통으로 일그러진 여자의 얼굴 위로 짙은 음영이 드리워진다.

- 어리석은 인간이로군. 이렇게 될 줄 몰랐나?

아득한 높이에서 울려 퍼지는 흑룡의 물음에, 그녀가 피가래를 뱉으며 대답했다.



- 아니, 알았지.

- 그런데 왜?

- 우리는 이걸 용기라고 배웠거든. 어리석은 게 아니라.

- 좋아. 그렇다면 용감한 인간이여, 지금이라도 나를 따를 생각은 없나?

- 좆 까. 이 괴물 자식아. 그리고…….



여자가 피에 젖은 이빨을 드러내며 웃었다.



- 내 이름은 파이 첸이다. 그냥 인간이 아니라, 파이 첸이라고.

- 기억해 두지, 인간.

- 그러는 게 좋을 거야. 조만간 어떤 대단한 녀석이 널 찾아와서 그 이름을, 이름을 물어, 볼…….



흐릿해진 목소리와 함께 헐떡이던 숨이 멈춘다.

초점을 잃은 동공이 텅 빈 허공을 응시한다.

여자. 아니, 파이 첸은 그렇게 죽었다.

홍콩이 자랑하던 S급 헌터이자 지난 대격변의 영웅이며, 내 친구였던 그녀가 죽었다.

지금으로부터 일주일 전에.



‘다 같이 술 한잔할까?’



문득 떠오른다.

아크 리치 토벌을 위해 쓰촨에서 처음 만난 날, 술자리를 제안하던 그녀의 모습이.

왜 하필 오늘이냐며 묻던 내게 돌아왔던 대답이.



‘술은 이런 날에 마시는 거란다.’

‘네?’

‘마지막이 될지도 모르잖니.’



그날, 우리는 코가 삐뚤어지도록 마셨다.

이것이 정말 마지막 술자리가 되리라곤 생각지도 못한 채.

“좋은 사람이었지.”

불현듯 울려 퍼진 한마디가 상념을 깨트린다.

매직 존슨의 굵은 저음과는 조금 다른, 쇳소리가 섞인 음성.

“훌륭한 헌터였고.”

나는 불청객의 정체를 묻지 않았다.

모니터 룸의 문이 열리기도 전에 한 걸음 앞서 스며든 매캐한 시가 냄새가, 목소리의 주인이 누구인지 알려주었으니까.

“그녀의 희생 덕분에 수많은 사람이 목숨을 건졌어. 수치스럽게 살아 돌아온 어느 병신도 그중 하나였지.”

척 헤이글.

엉클 척(Uncle Chuck)이라고도 불리는 그가 천천히 다가와 내 어깨를 짚었다.

이제는 하나밖에 남지 않은 오른팔로.

“깨어나자마자 그런 생각이 들더군. 파이 첸 대신 내가 죽었어야 했다고.”

“……헤이글.”

“알아. 전부 의미 없는 개소리라는 거. 그리고 나는 이 개소리를 지금껏 수백, 아니 수천 번도 넘게 반복해 왔지.”

척 헤이글은 시가 연기를 내뿜으며 씁쓸하게 웃었다.

수십 여개의 홀로그램 화면 속에서 끊임없이 재생되는 누군가의 죽음과 낯익은 얼굴들을 바라보면서.

“두 번 다시 그때와 같은 일이 벌어지게 놔두지 않겠다고 다짐했는데……. 결국 이렇게 됐군.”

무슨 말을 해야 할까.

아니, 감히 내가 무슨 말을 할 수 있을까.

내가 필요로 할 때마다 망설임 없이 달려와 주었던 그들과 달리, 나는 그들이 필요로 할 때 함께 있어 주지 못했다.

모르고스의 소환을 막지 못했고, 시간의 축이 뒤틀린 것 또한 빠르게 알아차리지 못했다.

그리고 이것이 그 결과다.

지난 열흘간 무차별적으로 자행된 수많은 파괴와 죽음.

그 모든 것이 감당 못 할 무게가 되어 내 가슴을 짓눌렀다.

뱃속 깊은 곳에서 용암처럼 들끓어 오르는 분노도 함께.

“그거 알아요?”

나는 참았던 숨을 토해 냈다.

이성과 감정이 뒤섞이고, 이내 머릿속이 차갑게 식는다.

그와 동시에, 눈앞에서는 또 한 번 죽음을 맞이하는 파이 첸의 모습이 재생되고 있다.

“지금부터, 그 누구도 희생하게 두진 않을 겁니다.”

나는 뜨겁게 달아오른 눈으로 화면 속 그녀를 바라보았다.

당장이라도 끊어질 듯한 숨결로, 모르고스에게 누군가의 등장을 경고하는 그녀의 모습을.

그래.

정말로, 그리될 것이다.
```

## Final English reading copy

```markdown
# Chapter 1152

There are no secrets in modern society.

There are cameras and the internet everywhere, and countless pieces of information spread across the world through them.

And sometimes, there are truths that are better left unknown.

Like a Pandora’s box that should never have been opened.

—KABOOOOOM!

The screen went black after one last deafening roar, too terrible to be captured in its entirety even by the speakers.

The viewers watching a famous influencer’s livestream from near the Kremlin instinctively realized that the video, which had just passed one hundred million simultaneous viewers, had made internet-broadcasting history—and that they would never see the influencer who had set this incredible record again.

“Oh, God.”

A single line suddenly appeared in the chat window, which had been frozen for several seconds. It was enough to explain everything they had seen and felt over the past thirty-odd minutes.

The dragon’s wings as it crossed the skies above Moscow, and Red Square vanishing without a trace.

Ironically, the creature had transformed into a human like them, slaughtered the Hunters and soldiers who blocked its way, and strode confidently into the Kremlin.

And then…

The disaster that engulfed Moscow.

Rrrrrumble!

The reverberation carried hundreds, even thousands of kilometers, shaking the world beyond the rectangular screen.

Countless eyes and ears—and even more cameras—captured the distant flash of light and the enormous mushroom cloud. The footage was immediately compiled into a single video and uploaded to the internet.

Its title conveyed the overwhelming despair and shock felt by humanity as the news from Moscow reached them.

—Where is God?

Where was God?

No one could answer that question.

No one.

They could only pray with all their hearts.

If God had truly abandoned them, then may someone appear who could save them.

No.

May he wake from his deep slumber as soon as possible.

Unlike God, who was so far away that their voices could not reach him, the savior of the new age answered their desperate pleas before long.

“He has returned.”

The whole world erupted once more at the first words spoken by the flushed-faced fifty-seventh President of the United States on the holographic TV.



* * *



The modern world meant something special to me.

It was the home where I’d been born and raised all my life—a place I could never forget.

That was why I’d always loved it.

Compared to Murim, where danger and trouble lurked around every corner, the modern world let me rest in relative peace.

But when had it started?

Everything began to go wrong, like a broken gear.

And the speed and fallout of that unraveling were worse and more horrifying than I could have imagined.

“So…”

What the hell was I supposed to say?

I kept trying to think, muttering words that meant nothing, but my mind had gone completely blank. Nothing came to me.

The hour-long video had just ended.

In the holographic footage, already paused, a black-haired man smiled faintly at the camera. I stared at him in silence.

Hoping someone would break the heavy quiet.

“I hear it happened three hours ago.”

At Magic Johnson’s low, subdued voice, the words I’d been holding back slipped past my dry lips.

“How many casualties?”

“……”

“Tell me. I’m prepared for it.”

Magic Johnson let out a quiet sigh before answering.

“At least twenty million, by the most conservative estimate.”

“Shit.”

“Moscow, and the surrounding cities in the metropolitan area, were swept away. We’ve thrown every resource we have at investigating, but…”

Magic Johnson trailed off and bit his lip.

“There are no signs of life. They’re probably all dead.”

Erasure.

The word flashed through my mind. It was also the most accurate way to describe what had happened.

“Vladimir. That fucking old man hid a hydrogen bomb in the Kremlin.”

At the start of the Great Cataclysm, humanity learned two very important things.

First:

No matter how airtight the security, modern science couldn’t stop spatial teleportation magic.

Second:

Spatial teleportation magic could move things, not just people.

Things like tactical nuclear weapons or hydrogen bombs.

That was why every nuclear-armed country in the world, led by the United States and Russia, had signed an international treaty and disposed of all weapons above a certain yield.

Or, to be precise, that was what we’d been told.

Until three hours ago, when a giant mushroom cloud swallowed the sky above Moscow.

“Russia is finished.”

That was true.

And for every other country, a different kind of beginning—and a crossroads—still lay ahead.

Would they resist to the bitter end?

Or surrender now and save their lives?

*Black Dragon Duke Morgoth.*

I murmured the name in my mind as I stared at the holographic screen.

On the land, blackened by magical power, a gigantic castle towered behind him. I took in his smiling face and burned it into my heart.

*Can I defeat him?*

The question came to me naturally. I realized my hand had clenched into a fist.

Dragon.

A monster without precedent, whose single appearance in the past had sent shock waves around the world.

But as his special title, Black Dragon Duke, suggested, Morgoth was no ordinary dragon.

*He’s strong. Horrifyingly strong.*

I turned my head and looked at the dozens of holographic screens filling the spacious monitor room, one after another.

They showed a predator that could bring down a forest of skyscrapers with a single flap of its wings, effortlessly deflect a barrage of magic, and trample Hunters underfoot.

Among those dying with one last scream were faces I knew.

“Die! Just die!”

On a crackling screen, a bloodied woman screamed.

Her lower body had already been crushed beyond recognition, and her stomach was split open, her entrails spilling out.

But, dazed, she kept drawing her bow at the rear of the retreating allies.

Until the dragon’s claws rushed in faster than an arrow and took both her arms too.

Crunch!

Blood spurted along with the severed flesh.

A deep shadow fell across the woman’s face, twisted with unbearable pain.

“You foolish human. Didn’t you know this would happen?”

The Black Dragon’s question rang down from high above. The woman spat blood and answered.

“I did.”

“Then why?”

“Because we were taught this is courage. Not foolishness.”

“Good. Then, brave human, will you still follow me?”

“Fuck off, you monster. And…”

The woman grinned, baring her blood-soaked teeth.

“My name is Pie Chen. I’m not just some human. I’m Pie Chen.”

“I’ll remember that, human.”

“You’d better. Soon, some amazing guy’s gonna come looking for you and ask about that name. Ask about my name, my—”

Her voice faded, and her panting stopped.

Her unfocused eyes stared into empty space.

The woman—no, Pie Chen—died just like that.

She was an S-rank Hunter Hong Kong was proud of, a hero of the last Great Cataclysm, and my friend.

She’d died a week ago.

*How about we all grab a drink?*

The memory surfaced without warning.

The day we first met in Sichuan to hunt the Arch Lich. She’d suggested we get together for drinks.

I’d asked her, “Why today of all days?” Her answer came back to me.

“Today’s the kind of day you drink.”

“Huh?”

“It might be our last chance.”

That day, we drank until we could barely stand.

Never once thinking it really might be our last drink together.

“She was a good person.”

A voice suddenly broke into my thoughts.

It was rough and gravelly, a little different from Magic Johnson’s deep voice.

“And a great Hunter.”

I didn’t ask who the unexpected visitor was.

The acrid smell of cigar smoke had seeped in a step ahead of him, before the door to the monitor room even opened. I knew who the voice belonged to.

“Thanks to her sacrifice, a lot of people survived. Even one bastard who came back alive in disgrace was among them.”

Chuck Hagel.

Also known as Uncle Chuck, he approached slowly and put a hand on my shoulder.

With his right arm—the only one he had left.

“The moment I woke up, I thought I should’ve died in Pie Chen’s place.”

“...Hagel.”

“I know. It’s all meaningless bullshit. And I’ve repeated that bullshit hundreds—no, thousands of times by now.”

Chuck Hagel blew out a cloud of cigar smoke and gave a bitter smile.

He looked at the familiar faces and the deaths playing over and over on the dozens of holographic screens.

“I swore I’d never let something like that happen again… And now look.”

What was I supposed to say?

No. What right did I have to say anything?

Whenever I needed them, they came running without hesitation. But when they needed me, I hadn’t been there.

I hadn’t stopped Morgoth from being summoned, and I hadn’t realized soon enough that the axis of time had shifted.

And this was the result.

The destruction and deaths carried out indiscriminately over the past ten days.

All of it weighed on my heart, heavier than I could bear.

Along with the anger roiling deep in my gut like lava.

“You know what?”

I let out the breath I’d been holding.

Reason and emotion tangled together, and then my mind turned cold.

At the same time, Pie Chen died again before my eyes.

“From now on, I won’t let anyone else be sacrificed.”

I stared at her on the screen, my eyes burning.

At her, using what little breath she had left to warn Morgoth that someone was coming for him.

Yes.

That’s exactly what would happen.
```
